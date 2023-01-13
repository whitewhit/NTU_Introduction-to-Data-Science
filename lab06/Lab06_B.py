import skimage
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage import color
from skimage import segmentation


# Do NOT modifify the function names

def fade_gradually(img):
    processed = img.copy()

    processed = skimage.img_as_float(img)

    processed_gray = color.rgb2gray(processed)

    width = img.shape[1]

    # use sigmoid function
    gray_gradually_coefficient = 1 / (1 + np.exp(-np.linspace(-10, 10, width)))

    gray_part = (processed_gray * gray_gradually_coefficient)[:, :, np.newaxis] 
    color_part = processed * (1 - gray_gradually_coefficient)[np.newaxis, :, np.newaxis] 

    processed_final = gray_part + color_part
    
    return processed_final


def image_matting(img):
    processed = img.copy()

    gray_img = np.mean(processed[:, :, :3], axis=2)

    mask = segmentation.flood(gray_img, (0, 0), tolerance=10)

    x = 255
    alpha = np.where(mask, 0, x)

    return np.dstack((processed, alpha))




# You are incouraged to test your program in the main function

def main():
    img1 = io.imread("monkey_island.jpg")
    img1_fade = fade_gradually(img1)

    img2 = io.imread("cat.jpg")
    img_mat = image_matting(img2)

    fig = plt.figure(figsize=(8,6))
    ax = []
    gs = fig.add_gridspec(2, 2, hspace=0.5, wspace=1.3)

    ax.append(fig.add_subplot(gs[0, 0]))
    ax.append(fig.add_subplot(gs[1, 0]))
    ax.append(fig.add_subplot(gs[1, 1]))

    x = ax[0]
    x.set_title("gradually fade from color to grayscale")
    x.imshow(img1_fade)

    x = ax[1]
    x.set_title("original")
    x.imshow(img2)

    x = ax[2]
    x.set_title("After image matting")
    x.imshow(img_mat)

    plt.show()

if __name__ == "__main__":
    main()


