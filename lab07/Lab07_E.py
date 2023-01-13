import skimage
import numpy as np
import matplotlib.pyplot as plt

from skimage import io, color, filters, transform, feature


def scan_document(img):

    gray_img = color.rgb2gray(img)

    corners = np.asarray([[122, 172], [63, 527], [315, 532], [280, 165]])
    dists = np.asarray([np.sqrt(np.add.reduce((a - b) ** 2)) for a, b in
                        zip([corners[-1], *corners[:-1]], corners)])
    w = int(np.mean(dists[[0, 2]]))
    h = int(np.mean(dists[[1, 3]]))
    t = transform.ProjectiveTransform()
    src = np.asarray([[0, 0], [0, h], [w, h], [w, 0]])
    dst = np.asarray(corners)
    t.estimate(src, dst)
    warped_img = transform.warp(gray_img, t, output_shape=[h, w])

    enhanced_img = warped_img + filters.laplace(warped_img)
    enhanced_img /= np.maximum.reduce(np.maximum.reduce(np.abs(enhanced_img)))

    local_thresh = filters.threshold_sauvola(enhanced_img, window_size=15)
    local_binary = enhanced_img > local_thresh

    # return warped_img, local_binary
    return local_binary


def main():
    img = io.imread('invoice.jpg')
    scanned = scan_document(img)
    io.imshow_collection([img, scanned], cmap='gray')
    io.show()


if __name__ == "__main__":
    main()
