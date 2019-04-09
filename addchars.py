#!/usr/bin/python3

from addcharslib import *

for f in faces:

    workshop = 1.4
    upm2048 = 1000.0/2048.0
    upm1000 = 1.0
    scale2048 = str(upm2048/workshop)
    scale1000 = str(upm1000/workshop)

    for sn in stylesName:
        modifyFile(scale1000, 'sourcesans', f, sn)
        modifyFile(scale2048, 'charis', f, sn)
