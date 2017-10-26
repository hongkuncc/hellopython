#encoding:utf-8
# try :
#     a=1
#     b=0
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print('抛出异常')
# else:
#     print('没有抛出异常的话会执行这行代码')
# finally:
#     print('不管有没有抛出异常都会执行这里的代码1')
# print('这个except语句只会捕获ZeroDivisionError异常')

# except ZeroDivisionError:
#     print('这个except语句只会捕获ZeroDivisionError异常')
# except NameError:
#         print('这个except语句只会捕获NameError异常')

#多个异常使用元组的形式
# except(ZeroDivisionError,NameError):
#     print('这个except语句会捕获ZeroDivisionError和NameError异常')

#如果不知道会具体抛出什么异常，就使用Exception来接受所有异常
# except Exception as error:
#         print('不管抛出了什么异常，都会执行这里的代码')
#         print(error)

#如果出现了不该出现的，抛出一个异常

# def greet(name, age):
#     if type(name) != str:
#         raise ValueError('name必须为str类型')
#     if type(age) != int:
#         raise ValueError('age必须为int类型')
#
#
# try:
#     greet('chk', '18')
# except ValueError as error:
#     print(error.args)

#自定义异常
class ArgumentError(Exception):
    def __init__(self,*args,**kwargs):
        super(ArgumentError,self).__init__(*args,**kwargs)
        # self.args = args
        print('参数错误')


def greet(name,age):
    if type(name) != str or type(age) != int:
        raise ArgumentError('参数类型错误')
    print('my name is:%s，my age is:%s' % (name,age))


try:
    greet('chk','18')
    raise ArgumentError('name必须为str类型')
except Exception as error:
    print(error.args)