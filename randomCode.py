# --------------------------------------#
#
# Created by Fu4ng on 2017/7/23.
#
# 博文地址:
# --------------------------------------#

# 　用random模块制作验证码

import random


def randomCode():
    ' 生成6位验证码 '
    code = []
    for i in range(6):
        # 生成数字
        if i == random.randint(0, 4):
            code.append(i)
        else:
            code.append(chr(random.randint(65, 90)))
    return code


print(randomCode())
