# --------------------------------------#
#
# Created by Fu4ng on 2017/7/20.
#
# 博文地址:
# --------------------------------------#

'''
找到解决方法了。使用fileinput模块
'''
import sys
import fileinput
lockLimit = 3


def log(name, psw):
    '登录函数'
    user_info = []
    with open('user.txt', 'r+') as user:
        for i in user.readlines():
            us, up, ut = i.strip('\n').split()
            user_info = us +' '+ up+' ' + ut
            if us == name and up == psw:
                print('登录成功！')
                return True
            elif us == name and up != psw:
                print('密码错误')
                break
            else:
                continue
    addTime(user_info)


def addTime(user_info):
    for line in fileinput.input('user.txt',inplace=1):
        print(line.replace(user_info,user_info[:-1]+str(int(user_info[-1])+1)).strip())
    if int(user_info[-1])%3 >=2:
        addLockedCount(user_info)

def addLockedCount(user_info):
    i = str(user_info).split()
    with open('locked.txt','a') as f:
        f.write(i[0])
    print("你的账户已被锁定！")
    for line in fileinput.input('user.txt',inplace=1):
        print(line.replace(user_info,user_info[:-1]+'0').strip())



def checkloked(name):
    '检查账户是否被锁,被锁返回True'
    with open('locked.txt', 'r') as f:
        for i in f.readlines():
            if name == i.strip('\n'):
                print('被锁了！')
                sys.exit()





name = input('你的用户名：')
pw = input('你的密码：')
checkloked(name)
f = log(name, pw)
