#coding:utf-8
#4名犯罪嫌疑人，其中一名是小偷，a说我不是小偷；b说c是小偷；
# c说小偷肯定是d；d说c胡说。其中三个真话，一个假话，谁是小偷？
for thief in ['a','b','c','d']:
    sum=(thief!='a')+(thief=='c')+(thief=='d')+(thief!='d')
    if sum==3:
        print"小偷是：%s" % thief