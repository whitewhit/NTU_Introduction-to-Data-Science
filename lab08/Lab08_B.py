import numpy as np
from skimage.color import rgb2gray
from skimage import io, filters, measure, morphology
from skimage.morphology import disk, square, rectangle, diamond
import matplotlib.pyplot as plt

rice = io.imread("SingleRice.jpg")
rice_gray = rgb2gray(rice)
otsu_thresh = filters.threshold_otsu(rice_gray)
otsu_binary = rice_gray > otsu_thresh

# 調整侵蝕與膨脹模型及大小
selem1 = square(10)
selem2 = disk(10)

otsu_binary_erosion = morphology.binary_erosion(otsu_binary, selem1)
otsu_binary_erosion_dilation = morphology.binary_dilation(otsu_binary_erosion, selem2)

contours = measure.find_contours(otsu_binary_erosion_dilation, 0.6)

fig, ax = plt.subplots()
ax.imshow(rice)

# 找出所有邊界
# for contour in contours:
#     ax.plot(contour[:, 1], contour[:, 0], linewidth=2, color='red')


# 找出最大的邊界
contour = sorted(contours, key=lambda x: len(x))[-1]
ax.step(contour.T[1], contour.T[0], linewidth=3, c='r')


ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

