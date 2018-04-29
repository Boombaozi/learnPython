age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('sdsd')
    print('sdsd')

# if判断条件还可以简写，比如写：
x = 1
if x:
    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。


birth = input('birth: ')
# 将输入的字符串转成Int类型
birth =int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')
