# --------------------------------------#
#
# Created by Fu4ng on 2017/7/24.
#
# 博文地址:
# --------------------------------------#

import re

with open('k.txt', 'r+') as f:
    name = 'bob'
    pw = '123456'
    t = '0'
    f.write(re.sub(r'{0}'.format(name + ' ' + pw + ' ' + t),r'{0}'.format(name + ' ' + pw + ' ' + str(int(t)+1)),f.read()))

