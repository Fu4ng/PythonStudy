# --------------------------------------#
#
# Created by Fu4ng on 2017/7/20.
#
# 博文地址:
# --------------------------------------#


import sys

lockLimit = 3


def log(name, psw):
    '登录函数'
    with open('user.txt', 'r+') as user:
        for i in user.readlines():
            us, up, ut = i.strip('\n').split()
            if us == name and up == psw:
                print('登录成功！')
                return True
            elif us == name and up != psw:
                print('密码错误')
                addLockCount(name)
                return False
            else:
                continue


def checkloked(name):
    '检查账户是否被锁,被锁返回True'
    with open('locked.txt', 'r') as f:
        for i in f.readlines():
            if name == i.strip('\n'):
                print('被锁了！')
                sys.exit()


def addLockCount(name):
    '密码出错三次,添加到被锁账户中'
    with open('user.txt', 'r+') as u:
        for line in u.readlines():
            i = line.split()
            if name == i[0]:
                line = line.replace(' {0}'.format(i[2]), ' {0}'.format(str(int(i[2]) + 1)))
                if int(i[2]) == lockLimit - 1:
                    line = line.replace('{0}'.format(i[2]), '0')
                    u.write(line)
                    with open('locked.txt', 'a') as l:
                        l.write(name)


name = input('你的用户名：')
pw = input('你的密码：')
checkloked(name)
f = log(name, pw)
