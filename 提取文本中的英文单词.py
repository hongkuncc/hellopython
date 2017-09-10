#_*_*coding=utf-8 _*_8
import re
f1 =open('giterror.txt','r')
data=f1.read()
f1.close()#打开文件，读入文本
result=re.findall('[A-z]+',data)#正则表达式的findall
result.sort()#排序
data='\n'.join(result)#把排序后的结果用换行符连成一段文本
f2=open('to.txt','w')
f2.write(data)
f2.close()#输出



