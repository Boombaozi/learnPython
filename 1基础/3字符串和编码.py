# python 使用 Unicode 编码
print('我爱JAVA')

# 将字符转化为实际二进制数的十进制表示
print(ord('c'))
print(ord('我'))

print('\u4e2d\u6587')

# 单字节
x = b'ABC'
print(x)

# 转码和解码
print('ABC'.encode('ascii'))
temp = '中文'.encode('utf-8')
print(temp)
print(temp.decode('utf-8'))

# 查看字符串长度

temp = len('中文')
print(temp)
# 2
print(len('中文'.encode('utf-8')))
# 6

# 通常加入这两行
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 格式化字符串
# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
a = 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print(a)

# 含有%需要转义
print('growth rate: %d %%' % 7)

# 输出位数控制
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# format()
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入
# 的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
print('%.3f' % (85 / 72 - 1))
