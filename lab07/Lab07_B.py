import skimage
import numpy as np
import matplotlib.pyplot as plt

from itertools import product, zip_longest
from skimage import io, filters, feature, morphology
from skimage.restoration import denoise_tv_chambolle, denoise_bilateral, \
    denoise_wavelet
from scipy.signal import convolve2d

saturn = io.imread('saturn.jpg', as_gray=True)

imgs = []
titles = ['mean filter',
          'gaussian filter',
          'total variation filter',
          'bilateral filter',
          'wavelet filter']

mean = skimage.img_as_ubyte(saturn, force_copy=True)
gaussian = skimage.img_as_float(saturn, force_copy=True)
total_variation = skimage.img_as_float(saturn, force_copy=True)
bilateral = skimage.img_as_float(saturn, force_copy=True)
wavelet = skimage.img_as_float(saturn, force_copy=True)

for i in range(3):
    mean = filters.rank.mean(mean, morphology.square(3))
    gaussian = filters.gaussian(gaussian, multichannel=False)
    total_variation = denoise_tv_chambolle(total_variation, multichannel=False)
    bilateral = denoise_bilateral(bilateral, multichannel=False)
    if i < 2:
        wavelet = denoise_wavelet(wavelet, multichannel=False)
    else:
        wavelet = None
    imgs.append(mean)
    imgs.append(gaussian)
    imgs.append(total_variation)
    imgs.append(bilateral)
    imgs.append(wavelet)

fig: plt.Figure = plt.figure(figsize=(20, 20))
gs: plt.GridSpec = fig.add_gridspec(3, 5)
ax: list[plt.Axes] = [fig.add_subplot(gs[i, j]) for i, j in
                      product(range(3), range(5))]

for i, (x, img, title) in enumerate(zip_longest(ax, imgs, titles)):
    if img is not None:
        x.set_title(title, size=18)
        x.set_xticks([])
        x.set_yticks([])
        x.imshow(img, cmap='gray')
    else:
        x.axis('off')

for i, y in enumerate([.225, .5, .775]):
    fig.text(0.05, y, f'{3 - i}', ha="center", va="center", size=18)

fig: plt.Figure = plt.figure(figsize=(20, 20))
gs: plt.GridSpec = fig.add_gridspec(2, 4, wspace=0.05, hspace=0.05)
ax: np.ndarray = np.asarray([fig.add_subplot(gs[i, j]) for i, j in
                             product(range(2), range(4))]).reshape((2, 4))

for x in ax.flatten():
    x.axis('off')

ax[0, 0].set_title(r'A.    total_variation(wavelet(original))', size=14)
ax[0, 0].imshow(denoise_tv_chambolle(denoise_wavelet(saturn)), cmap='gray')
ax[0, 1].set_title(r'B.    wavelet(total_variation(original))', size=14)
ax[0, 1].imshow(b := denoise_wavelet(denoise_tv_chambolle(saturn)),
                cmap='gray')  #
ax[0, 2].set_title(r'C.    total_variation(gaussian(original))', size=14)
ax[0, 2].imshow(denoise_tv_chambolle(filters.gaussian(saturn)), cmap='gray')
ax[0, 3].set_title(r'D.    gaussian(total_variation(original))', size=14)
ax[0, 3].imshow(filters.gaussian(denoise_tv_chambolle(saturn)), cmap='gray')  #

ax[1, 0].set_title(r'E.    wavelet(B)', size=14)
ax[1, 0].imshow(denoise_wavelet(b), cmap='gray')
ax[1, 1].set_title(r'F.    sobel(B)', size=14)
ax[1, 1].imshow(filters.sobel(b), cmap='gray')
ax[1, 2].set_title(r'G.    B + F', size=14)
ax[1, 2].imshow(b + filters.sobel(b), cmap='gray')  #
ax[1, 3].set_title(r'H.    E + sobel(E)', size=14)
ax[1, 3].imshow(denoise_wavelet(b) + filters.sobel(denoise_wavelet(b)),
                cmap='gray')

plt.show()