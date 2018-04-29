#继承object类

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    pass

a = Student(1,2)

# 对象的内存地址
print(a)
print(a.name)

# 方法的内存地址
print(a.__init__)