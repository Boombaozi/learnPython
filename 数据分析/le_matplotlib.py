import matplotlib.pyplot as plt
import numpy as np


x = [1,2,3,4]
y1 = [4,8,2,6]
y2 = [10,12,5,3]

# 数据a
plt.plot(x,y1,"ro--",label="股票a")
plt.plot(x,y1,"g.-",label="股票c")
# 数据b
plt.plot(x,y2,"b^--",label="股票b")

plt.xticks([1,2,3,4,5,6,7,8,9,10])
# plt.yticks(np.range(2,100,1))

# 显示标注
plt.legend()
plt.title("折线图")
plt.xlabel("x label")
plt.ylabel("y label")
plt.grid()

# 展示图的一部分
# plt.xlim()
# plt.ylim()

# 图像展示
plt.show()




