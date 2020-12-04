import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# def randrange(n, vmin, vmax):
#     '''
#     Helper function to make an array of random numbers having shape (n, )
#     with each number distributed Uniform(vmin, vmax).
#     '''
#     return (vmax - vmin)*np.random.rand(n) + vmin

# n = 100

# # For each set of style and range settings, plot n random points in the box
# # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m, s=40)

ax.scatter(0, 0, 0, c="g", marker="o", s=50)
ax.scatter(1, 0, 0, c="g", marker="o", s=50)
ax.scatter(0, 1, 0, c="g", marker="o", s=50)
ax.scatter(1, 1, 0, c="g", marker="o", s=50)
ax.scatter(-1, 0, 0, c="g", marker="o", s=50)
ax.scatter(0, -1, 0, c="g", marker="o", s=50)
ax.scatter(-1, -1, 0, c="g", marker="o", s=50)
ax.scatter(-1, 1, 0, c="g", marker="o", s=50)
ax.scatter(1, -1, 0, c="g", marker="o", s=50)

plt.show()
time.sleep()