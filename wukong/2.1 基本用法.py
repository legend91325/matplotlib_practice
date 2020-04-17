import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = x**2
y = 2*x+1
plt.plot(x, y)
plt.show()