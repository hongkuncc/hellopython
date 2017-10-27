#encoding:utf-8
# num_list = (x for x in range(1,10000))
# print(type(num_list))

# 自己写生成器
# def my_gen():
#     yield 1
#     yield 2
#     yield 3
#
# ret=my_gen()
# print(next(ret))
# print(next(ret))
# print(next(ret))

#send 方法
# def my_gen(start):
#     while start<10:
#        temp = yield start
#         print(temp)
#        start+=1
#
#
# ret=my_gen(1)
# for x in ret:
#     print(x)
# # print(next(ret))
# #
# # print(ret.send('hello world'))

