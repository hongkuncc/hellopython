#encoding:utf-8
source=raw_input(u'请输入图片地址：'.encode('gbk'))
des=raw_input(u'请输入目标地址'.encode('gbk'))
with open(source,'r') as fp1:
    with open(dest,'w') as fp2:
        for x in fp1:
            fp2.write(x)

print('恭喜图片复制完成！')