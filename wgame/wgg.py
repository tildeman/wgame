import dispimg
import imgget
import sys
imgget.makeq()
r=imgget.r
for x in r:
    if dispimg.display(*x)==0:sys.exit()
