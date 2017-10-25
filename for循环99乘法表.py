#encoding:utf-8
from __future__ import print_function

for row in range(1,10):
    for column in range(1,row+1):
        print("%d*%d=%d"%(column,row,column*row),end=' ')
    print("")
