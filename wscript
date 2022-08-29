#!/usr/bin/python3
# this is a smith configuration file

# asika

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-p'}, # do not run psfix on the final fonts
    {'opt' : '-s'}  # only build a single font
    )

import os2

# set the default output folders
out='results'

# locations of files needed for some tasks
DOCDIR = ['documentation', 'web']

# set meta-information
script='orya'
APPNAME='nlci-' + script

DESC_SHORT='Oriya Unicode font with OT support'
DESC_NAME='NLCI-' + script
getufoinfo('source/Asika-Regular.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# set fonts to build
faces = ('Asika',)
facesLegacy = ('asik',)
styles = ('-R', '-B', '-I')
stylesName = ('Regular', 'Bold', 'Italic')
stylesLegacy = ('', 'bd', 'i')

if '-s' in opts:
    faces = (faces[0],)
    facesLegacy = (facesLegacy[0],)
    styles = (styles[0],)
    stylesName = (stylesName[0],)
    stylesLegacy = (stylesLegacy[0],)

# set build parameters
fontbase = 'source/'
archive = fontbase + 'archive/unhinted/'
generated = 'generated/'
tag = script.upper()

panose = [2, 0, 0, 3]
codePageRange = [0, 29]
unicodeRange = [0, 1, 2, 3, 4, 5, 6, 7, 15, 19, 29, 31, 32, 33, 35, 38, 39, 40, 45, 60, 62, 67, 69, 91]
hackos2 = os2.hackos2(panose, codePageRange, unicodeRange)

if '-l' in opts:
    for f, fLegacy in zip(faces, facesLegacy):
        for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
            added = '../' + archive + fLegacy.upper() + sLegacy.upper() + '.ttf'
            font(target = process('ufo/' + f + '-' + sn.replace(' ', '') + '.ttf',
                    cmd(hackos2 + ' ${DEP} ${TGT}'),
                    name(f, lang='en-US', subfamily=(sn))
                    ),
                source = legacy(f + s + '.ttf',
                                source = archive + fLegacy + sLegacy + '.ttf',
                                xml = fontbase + 'asika_unicode.xml',
                                params = ' -f ' + added,
                                noap = '')
                )

if '-l' in opts:
    faces = list()
for f in faces:
    p = package(
        appname = APPNAME + '-' + f.lower(),
        version = VERSION,
        docdir = DOCDIR # 'documentation'
    )
    for dspace in ('Roman', 'Italic'):
        designspace('source/' + f + dspace + '.designspace',
            target = process('${DS:FILENAME_BASE}.ttf',
                cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo']),
            ),
            opentype = fea(generated + '${DS:FILENAME_BASE}.fea',
                mapfile = generated + '${DS:FILENAME_BASE}.map',
                master = fontbase + 'master.feax',
                make_params = ''
                ),
            #graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2',
            #    params =  '-e ${DS:FILENAME_BASE}_gdlerr.txt'
            #    ),
            # classes = fontbase + 'asika_classes.xml',
            # ap = generated + '${DS:FILENAME_BASE}.xml',
            version = VERSION,
            woff = woff('woff/${DS:FILENAME_BASE}', type='woff2',
                metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml'),
            script = 'ory2', # 'orya'
            # package = p,
            pdf = fret(params = '-oi')
        )
