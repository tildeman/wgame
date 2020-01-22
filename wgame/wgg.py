import dispimg
import imgget
import sys
import os
os.chdir(__file__[:-6])
imgget.makeq()
r=imgget.r
for x in r:
    if dispimg.display(*x)==0:sys.exit()
