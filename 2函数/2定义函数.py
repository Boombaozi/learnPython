# 定义函数

# a=my()

def my():
    x = int(input())
    if x >= 0:
        print('x>=0')
    else:
        print('x<0')


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：

def nop():
    pass


# pass还可以用在其他语句里，比如：

# if age >= 18:
#     pass

# 参数检查

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值,函数可以同时返回多个值，但其实就是一个tuple

# 比如在游戏中经常需要从一个点移动到另一个点，
# 给出坐标、位移和角度，就可以计算出新的新的坐标：

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print('%.2f%.2f' % (x, y))
