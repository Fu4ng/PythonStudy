# --------------------------------------#
#
# Created by Fu4ng on 2017/7/20.
#
# 博文地址:
# --------------------------------------#


import sys

lockLimit = 3
user = open('user.txt', 'r+')
flag = 0
# 格式化数据
data = {}
for i in user.readlines():
    i = i.strip('\n').split()
    data[i[0]] = {}
    data[i[0]]['pw'] = i[1]
    data[i[0]]['time'] = int(i[2])
user.close()
while flag == 0:
    lockCount = open('locked.txt', 'r+')
    user = open('user.txt', 'r+')
    userName = input('Your name:')
    # 检查是否被锁
    l_flag = 0
    for line in lockCount.readlines():
        if userName in line: l_flag = 1
    if l_flag == 1:
        print('%s has be locked! ' % userName)
        continue
    # 检查是否在用户名内
    u_flag = 0
    for line in user.readlines():
        if userName in line: u_flag = 1
    if u_flag == 0:
        print('sorry,no find your name! ')
        continue
    # 文件指针回到开头
    user.seek(0)
    # 检查密码是否匹配
    userPw = input('your pw :')
    if data[userName]['pw'] == userPw:
        print('login successfully ! \n')
        flag = 1
        break
    else:
        print('your pw worry!')
        data[userName]['time'] += 1
        if data[userName]['time'] >= lockLimit:
            print('%s has be locked !\n ' % userName)
            lockCount.write(userName)
            for line in user.readlines():
                line = line.strip('\n').split()
                if line[0] == userName: line[2] = str(data[userName]['time'])
    lockCount.close()
    user.close()
    if flag == 1: break
