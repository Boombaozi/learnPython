# list python内置的数据类型,有点类似JAVA中的ArrayList但是是完全不同的实现方式

ss = [1, 2, 3, 4, 5]

int
n = 0
while n < len(ss):
    print(ss[n])
    n += 1

# 可以使用-1作索引
print(ss[-1])

# 追加元素到末尾
ss.append(6)
print(ss)
# 插入元素到指定位置,其余元素会相应的后移
ss.insert(1, 100)
print(ss)

# 删除末尾元素

ss.pop()
print(ss)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：

ss.pop(1)
print(ss)

# tuple另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

sss = (1, 2, 3, 4)
sss[0]=12
print(sss)

