# dict  相当于是 java 中的map
d = {'a': 5, 'b': 7, 'c': 8}

# print(d['Bob'])
# 如果key不存在，dict就会报错：

d.get(' Bob')

d.pop('a')


print(d)

# 要创建一个set，需要提供一个list作为输入集合

s = set([1, 2, 3, 3, 2, 1, 4, 2, 3, ])
print(s)

s.add(1)

s.remove(4)

print(s)
