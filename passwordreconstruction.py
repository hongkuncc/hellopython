#encoding:utf-8
import getpass
import hashlib
FILE_NAME='password_book.txt'

def index_page():
    print("===欢迎进入密码管理系统===")
    print("0,退出系统")
    print("1,添加新密码")
    print("2,查看所有密码")
    value=input('请输入你要做的操作：')
    while True
      if value=='0':
          break
      elif value=='1':
        pass
      elif value=='2':
        pass
      else:
        print('你输入的有误，请重新输入！')

def login_page():
    pwd=getpass.getpass('[登陆]请输入登录密码')
    hashed_pwd = hashlib.md5(pw1.encode('utf-8')).hexdigest()
    with open(FILE_NAME, 'r')as fp:
        line=fp.readline().replace('\n','')
        if line==hashed_pwd:
            #登陆成功
            index_page()
        else:
            #密码错误
            continue

def is_first_use():
    first = False
    try:
        with open(FILE_NAME, 'r') as fp:
            line = fp.readline()
        if line:
            first = False
        else:
            first = True
    except IndentationError:
        first = True


return first

def main():
    print('===密码管理系统===')
    if is_first_use():
        while True:
             pw1=getpass.getpass('请输入系统管理密码：')
             pw2 = getpass.getpass('请输入系统管理密码:')
             if pw1 != pw2:
                 print('两次密码不一样，请重新输入！')
             else:
                #把用户密码
                hashed_pwd=hashlib.md5(pw1.encode('utf-8')).hexdigest()
                with open(FILE_NAME,'w') as fp:
                   fp.write(hashed_pwd+'\n')
                break
    else:
         pass

    password=getpass.getpass('请输入系统管理密码：')
    print(password)

if __name__=='__main__':
    main()