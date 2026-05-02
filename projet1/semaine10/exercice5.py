import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = 2*x + 3
y3 = np.sin(x)

plt.plot(x, y1, color='blue', label='fonction quadratique')
plt.plot(x, y2, color='orange', label='fonction linéaire')
plt.plot(x, y3, color='green', label='fonction sinus')
plt.grid()
plt.legend()
plt.show()
