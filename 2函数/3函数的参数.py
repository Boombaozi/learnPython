# 可以设定默认参数

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

a= power(2)
print(a)

# 默认参数必须指向不变对象,

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def add_end2(L=[]):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())

print(add_end())

print(add_end2())

print(add_end2())

# 参数数量可变，实际是传了一个数组

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 如果已经有一个list或者tuple，
# 要调用一个可变参数怎么办？可以这样做：

nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])




