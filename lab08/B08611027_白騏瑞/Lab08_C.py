import numpy as np
import matplotlib.pyplot as plt

from skimage import io, filters, img_as_float
from scipy.signal import convolve2d

x_ray = img_as_float(io.imread('Xray.png', as_gray=True))

# a
x_ray_laplace = filters.laplace(x_ray)

# b
x_ray_sharpened = x_ray - x_ray_laplace

# c
x_ray_sobel = filters.sobel(x_ray_sharpened)

# d
average_filter = np.ones((5, 5)) / 25
x_ray_smooth = convolve2d(x_ray_sobel, average_filter, mode='same')

# e
x_ray_e = x_ray_sharpened * x_ray_smooth

# f
x_ray_enhanced = x_ray + x_ray_e

# g
x_ray_contrast = np.power(x_ray_enhanced, 0.5)


# plot the images
plt.figure(figsize=(10, 10))

plt.subplot(2, 4, 1)
plt.imshow(x_ray, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.xlabel('Original image')

plt.subplot(2, 4, 2)
plt.imshow(x_ray_laplace, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.xlabel('(a)')

plt.subplot(2, 4, 3)
plt.imshow(x_ray_sharpened, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.xlabel('(b)')

plt.subplot(2, 4, 4)
plt.imshow(x_ray_sobel, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.xlabel('(c)')

plt.subplot(2, 4, 5)
plt.imshow(x_ray_smooth, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.xlabel('(d)')

plt.subplot(2, 4, 6)
plt.imshow(x_ray_e, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.xlabel('(e)')

plt.subplot(2, 4, 7)
plt.imshow (x_ray_enhanced, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.xlabel('(f)')

plt.subplot(2, 4, 8)
plt.imshow( x_ray_contrast, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.xlabel('(g)')

plt.show()