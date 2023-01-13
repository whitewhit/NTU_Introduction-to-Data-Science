import scipy.spatial
import skimage
import numpy as np
import matplotlib.pyplot as plt

from skimage import io, exposure, filters, morphology as morph
from scipy.signal import convolve2d
from itertools import product

# Reconstruct image
img = io.imread('Fingerprint.tif', as_gray=True)
img = skimage.img_as_float(img)
img = morph.closing(img)
img = exposure.equalize_adapthist(img, 11)
img = filters.gaussian(img, sigma=0.5, truncate=5)

thresh = filters.threshold_sauvola(img, 9)
img_binary = img < thresh
img_binary = morph.remove_small_objects(img_binary, 20)

img_closed = morph.binary_closing(img_binary)
img_no_holes = morph.remove_small_holes(img_closed)

# skeleton
new_img = filters.gaussian(img_no_holes, truncate=3)
new_binary = new_img > filters.threshold_sauvola(new_img, 15)
new_binary = morph.binary_dilation(
    morph.remove_small_objects(
        morph.binary_erosion(new_binary), 4
    )
)
new_binary = np.where(
        convolve2d(new_binary, morph.square(3), mode='same') > 3, 1, 0)

skeleton = morph.skeletonize(new_binary)
# plt.imshow(skeleton, cmap='gray')
# plt.show()

# find bifurcation points
neighbors2 = convolve2d(skeleton,
                        np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
                        mode='same', boundary='fill')

terminations = np.asarray(np.where(np.logical_and(skeleton == 1,
                                                      neighbors2 == 1))).T

convex_hull = scipy.spatial.ConvexHull(terminations)
terminations = np.asarray([[j, i] for j, i in terminations
                               if (97 <= i <= 381) and (54 <= j <= 441)])

bifurcations = np.where(np.logical_and(skeleton == 1,
                                        neighbors2 == 3), 1, 0)


# remove duplicate bifurcation points
neighbors1 = convolve2d(bifurcations,
                        np.asarray([[0, 1, 0], [1, 0, 1], [0, 1, 0]]),
                        mode='same', boundary='fill')
bifurcations = np.asarray(np.where(
        np.logical_and(
        bifurcations == 1,
        np.logical_or(neighbors1 == 0, neighbors1 == 2)
        )
)).T

bifurcations = np.asarray([[j, i] for j, i in bifurcations if j <= 428])

imgs = [
    io.imread('Fingerprint.tif', as_gray=True),
    skeleton,
    np.where(np.logical_and(skeleton == 1, neighbors2 == 1), 1, 0),
    np.where(np.logical_and(skeleton == 1, neighbors2 == 3), 1, 0)
    ]

rows = 1
cols = 4
fig: plt.Figure = plt.figure(1, (16, 4.8))
gs: plt.GridSpec = fig.add_gridspec(rows, cols, wspace=0, hspace=0)
ax: list[plt.Axes] = [fig.add_subplot(gs[i, j]) for i, j in
                          product(range(rows), range(cols))]
plt.subplots_adjust(left=0, bottom=0, right=1, top=1)

for x, im in zip(ax, imgs):
    x.axis('off')
    x.imshow(im, cmap='gray')

for i in range(2):
    ax[i].plot(terminations[:, 1],
                   terminations[:, 0],
                   c='#00000000', lw=0, marker='o', ms=5, mec='#00FF00', mew=1)
    ax[i].plot(bifurcations[:, 1], bifurcations[:, 0],
                   c='#00000000', lw=0, marker='o', ms=5, mec='#FF0000', mew=1)
ax[2].plot(terminations[:, 1],
               terminations[:, 0],
               c='#00000000', lw=0, marker='o', ms=5, mec='#00FF00', mew=1)
ax[3].plot(bifurcations[:, 1], bifurcations[:, 0],
               c='#00000000', lw=0, marker='o', ms=5, mec='#FF0000', mew=1)

plt.show()