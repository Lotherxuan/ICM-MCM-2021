import matplotlib.pyplot as plt
import numpy as np

a = np.array([40, 50, 60, 70, 80, 90, 100])
b = np.array([0.48, 0.70, 0.85, 0.93, 0.98, 1.0, 1.0])
c = np.array([0.34, 0.44, 0.68, 0.79, 0.84, 0.89, 1.0])

plt.plot(a, b, marker='^', label='SA', c='red', ms=8)
plt.plot(a, c, marker='s', label='normal method', ms=8)
plt.xlabel('number of UAVs')
plt.ylabel('coverage rate')
plt.title("")
plt.legend()
plt.grid()
plt.show()