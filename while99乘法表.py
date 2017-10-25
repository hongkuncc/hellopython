#encoding:utf-8
#1共9行
#2每行列数，就是当前的列数
#乘法表第一个代表的是列，第二个是行
from __future__ import print_function
row=1
column=1

while row<=9:
    while column<=row:
        print ("%d*%d=%d"%(column,row,column*row),end =' ')
        column+=1
    print("")
#进行复位
    column=1
    row+=1