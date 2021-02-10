import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from scipy import interpolate

s = "0 .02 -.12 0 -2.09 0 -.58 -.08 0 0.0 2 0 0 -2.38 0 -4.96 0 0 0 -.1 0 .1 1 0 -3.04 0 -.53 0 .1 0 0 0 0 3.52 0 0 0 0 0 0 -.43 -1.98  0 0 0 .77 0 2.17 0 0 0 0 -2.29 0 .69 0 2.59 0 .3 0 -.09 -.31 0 0 0 4.27 0 0 0 -.01 0 0 0 5.13 7.4 0 1.89 0 .04 0  .1 0 .58 0 0 1.75 0 -.11 0 0  0 -.01 0 0 .3 0 0 0 0 .01"
l = s.split()
alt = []
for i in range(10):
    for j in range(10):
        alt.append([i, j, l[i * 10 + j]])

alt = np.array(alt)
X = alt[:, 0]
Y = alt[:, 1]
Z = alt[:, 2]
X = X.reshape((10, 10))
Y = Y.reshape((10, 10))
Z = Z.reshape((10, 10))
# temp=Z.flatten()
# for i in range(len(temp)):
#     temp[i]=float(temp[i])
# Z=temp.reshape((10,10))
X = X.astype(np.float)
Y = Y.astype(np.float)
Z = Z.astype(np.float)

f = interpolate.interp2d(X, Y, Z, kind='cubic')
X = np.arange(0, 9, 0.1)
Y = np.arange(0, 9, 0.1)
Z = f(X, Y)
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='rainbow')
#    linewidth=0, antialiased=False
# Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
# ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()