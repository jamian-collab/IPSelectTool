from getAddress import *
from ping import *

with open('ip.txt', 'r') as f:
    lines = f.readlines()
str = ''
for line in lines:
    if line != '':
        ip = line.strip('\n')
        addr = getAddress(ip) # 获取ip所在地址
        time = ping(ip) # 获取ping的平均时间
        if time:
            info = '%s\t%s\t%dms\n'%(ip, addr, time)
            print(info, end='')
            str += info
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(str)

wait = input('enter any key to end')