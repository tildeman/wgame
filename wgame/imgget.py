from imgdata import *
from random import choice
def makeq():
    global r
    r=[choice(x) for x in [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]]
    r=[('img\\l'+str(x+1)+'\\'+r[x][0]+'.gif',r[x][0],r[x][1],x+1) for x in range(len(r))]
    print(r)
if __name__=='__main__':
    makeq()
