import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0, 5, 0.125)
Y = np.arange(0, 5, 0.125)
X, Y = np.meshgrid(X, Y)
ux = uy = 2.5
sx = sy = 1
p = 0.1

x = (X - ux) / sx
y = (Y - uy) / sy
k = 2 * np.pi * sx * sy * np.sqrt(1 - p * p)

Z = np.exp(-(x * x + y * y - 2 * p * x * y) / (2 * (1 - p * p))) / k


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d', azim=-50, elev=50)

surf = ax.plot_surface(X, Y, Z, cmap='viridis',
                       linewidth=0, antialiased=False)

ax.set_xlim(0, 5)
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xlabel('X axis')

ax.set_ylim(0, 5)
ax.set_yticks([0, 1, 2, 3, 4, 5])
ax.set_ylabel('Y axis')

ax.set_zlim(0, 0.16)
ax.set_zticks([0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14])
ax.set_zlabel('Z axis')

plt.show()