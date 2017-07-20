# --------------------------------------#
#
# Created by Fu4ng on 2017/7/20.
#
# 博文地址:
# --------------------------------------#


import sys

lockLimit = 3
tryTimes = 0
login = 0
data = open('user.txt')
lock_count = open('locked.txt')
while tryTimes < lockLimit:
    userName = input('Your name:')
    userPw = input('Your passwords:')
    for line in lock_count:
        if userName == line:
            sys.exit()
    for line in data:
        line = line.split()
        if userName == line[0] and userPw == line[1]:
            print('login successful')
            login = 1
            break
        else:
            print('sorry,your passwords not right')
            tryTimes += 1
            break
    if login == 1: break
else:
    print('locked')
    addLockCount = open('locked.txt', 'a')
    addLockCount.write(userName)
