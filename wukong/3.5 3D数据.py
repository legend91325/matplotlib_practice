import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# pycharm s
fig = plt.figure()
ax = Axes3D(fig)
# X,Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.cos(R)
# rstide 行跨度 cstride 列跨度
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, edgecolor='black', cmap=plt.get_cmap('rainbow'))
# zdir='z' 理解为等高线在xoy平面的投影
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)
plt.show()
