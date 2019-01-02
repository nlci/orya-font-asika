#!/bin/python

from addcharslib import *

def modifySource(sfd, f, s, sn):
    print sfd

    workshop = 1.4
    upm2048 = 1000.0/2048.0
    upm1000 = 1.0
    scale2048 = '-s ' + str(upm2048/workshop) + ' '
    scale1000 = '-s ' + str(upm1000/workshop) + ' '

    asn = sn
    asn = asn.replace('BoldItalic', 'Bold')
    asn = asn.replace('Italic', 'Regular')
    cmd = scale2048 + '-i ' + annapurna + asn + '.ttf' + ' --rangefile cs/annapurna/main.txt'
    modifyFile(cmd, sfd)

    sns = s.replace('-', '')
    cmd = scale1000 + '-i ' + sophia + sns + '.ttf' + ' --rangefile cs/sophia/main.txt'
    modifyFile(cmd, sfd)
    cmd = scale2048 + '-i ' + charis + s + '.ttf' + ' --rangefile cs/charis/composite4sophia.txt --rangefile cs/charis/extra4sophia.txt'
    modifyFile(cmd, sfd)

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        sn = sn.replace(' ', '')
        modifySource(f + '-' + sn + '.sfd', f, s, sn)
