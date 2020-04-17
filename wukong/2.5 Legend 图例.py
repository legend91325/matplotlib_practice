import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()


# 设置坐标轴
plt.xlim((-1, 2))
plt.ylim((-2, 3))

plt.xlabel("I am X")
plt.ylabel("I am Y")
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# outward axes 百分比
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

l1, = plt.plot(x, y2, label='up')
# 颜色 线宽 线样式
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
#
plt.legend(handles=[l1, l2],labels=['aaa', 'bbb'], loc='best')

plt.show()
