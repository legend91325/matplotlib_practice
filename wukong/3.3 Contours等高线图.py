import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    # the height function
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# 将原始数据编程网格数据
X, Y = np.meshgrid(x, y)

# 填充颜色
# use plt.contourf to filling contours
# X,Y and value for (X,Y) point
# X, Y , Z  对应的 cmap 对应的颜色 plt.cm.hot or plt.cm.cold
# 8 显示等高线的密集程度，数值越大，画的等高线数就越多
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

# use plt.contour to add contour lines
# 等高线的线
# 8 显示等高线的密集程度，数值越大，画的等高线数就越多
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidths=.5)

# adding label
# 数字描述
plt.clabel(C, inline=True, fontsize=10)


plt.xticks(())
plt.yticks(())
plt.show()
