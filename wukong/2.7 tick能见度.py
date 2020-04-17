import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1 * x

plt.figure()
plt.plot(x, y, linewidth=10,zorder=1)
plt.ylim(-2, 2)

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# outward axes 百分比
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 把坐标轴数值拿出来 单个设置参数
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_zorder(2)
    # background color
    # alpha 透明度
    # edgecolor 边框颜色
    # zorder 图层顺序 数值最大的在顶层
    label.set_bbox(dict(facecolor='white'
                        , edgecolor='None'
                        , alpha=0.7
                        ))
plt.show()
