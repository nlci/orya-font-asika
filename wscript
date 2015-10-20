# asika

# set folder names
out='results'
TESTDIR='tests'
STANDARDS='tests/reference'

# set meta-information
script='orya'
APPNAME='nlci-' + script
VERSION='0.100'
TTF_VERSION='0.100'
COPYRIGHT='Copyright (c) 2009-2015, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Oriya Unicode font with OT support'
DESC_LONG='''
Pan Oriya font designed to support all the languages using the Oriya script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0b15'

# set fonts to build
faces = ('Asika',)
styles = ('-R', '-B', '-I')
stylesName = ('Regular', 'Bold', 'Italic')

# set build parameters
fontbase = 'source/'
tag = script.upper()

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        font(target = process(tag + f + '-' + sn.replace(' ', '') + '.ttf',
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + s + '.sfd',
            sfd_master = fontbase + 'master.sfd',
            opentype = internal(),
            #graphite = gdl(fontbase + f + s + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2 -l first',
            #    params = '-d -v2'
            #    ),
            #classes = fontbase + 'asika_classes.xml',
            ap = f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license = ofl('Asika', 'NLCI'),
            woff = woff(),
            script = 'orya',
            fret = fret(params = '-r')
        )
