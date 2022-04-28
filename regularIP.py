
import re
with open('ip.txt', 'r+', encoding='utf-8') as f:
    str = f.read()
pattern =re.compile(r'\d+\.\d+\.\d+\.\d+')  # 正则表达式，匹配IP地址
t = ''
for i in pattern.findall(str):
    t += i+'\n'
with open('ip.txt', 'w+', encoding='utf-8') as f:
    f.write(t)