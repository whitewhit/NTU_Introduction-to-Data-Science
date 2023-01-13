import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2hsv, hsv2rgb

YellowFan = io.imread("YellowFan.png")
width = YellowFan.shape[1]
height = YellowFan.shape[0]
img = np.zeros((height,width))

YellowFan_hsv = rgb2hsv(YellowFan)
img[np.logical_and(YellowFan_hsv[:, :, 0]>0.15, YellowFan_hsv[:, :, 0]<0.17)] = 255

plt.imshow(img, cmap='gray')
plt.show()