import skimage
import numpy as np
import matplotlib.pyplot as plt

from skimage import io, segmentation, color


# Do NOT modify the function names

def fade_gradually(img):
    # TODO_B1

    img = skimage.img_as_float(img)
    # FutureWarning: Non RGB image conversion is now deprecated.
    assert (img.ndim == 3)
    if img.shape[-1] == 4:
        gray_img = color.rgb2gray(color.rgba2rgb(img))
    elif img.shape[-1] == 3:
        gray_img = color.rgb2gray(img)
    else:
        raise ValueError
    ncol = img.shape[1]

    # gray_factor determines how gray each column is, using a sigmoid function
    gray_factor = 1 / (1 + np.exp(-np.linspace(-10, 10, num=ncol)))

    gray_part = (gray_img * gray_factor)[:, :, np.newaxis]  
    color_part = img * (1 - gray_factor)[np.newaxis, :, np.newaxis]
    return gray_part + color_part


def image_matting(img):
    # TODO_B2

    # img_magenta_bg = img.copy()
    # img_magenta_bg[np.where(np.all(img <= [8] * 3, axis=2))] = [255, 0, 255]

    # get the mean of the rgb values
    gray_img = np.mean(img[:, :, :3], axis=2)

    # assume: background color is #000000  
    # perform a flood fill operation, starting at (0, 0)
    # TODO deal with no background color in (0, 0)
    # TODO deal with unconnected background
    mask = segmentation.flood(gray_img, (0, 0), tolerance=10)
    

    x = 255
    if img.shape[-1] == 4:  # preserve alpha of non-background pixels
        x = img[:, :, 3]
    alpha = np.where(mask, 0, x)

    return np.dstack((img, alpha))


def my_resize(img, height, width, *, verbose=False):
    # TODO_B3

    img = skimage.img_as_float(img)

    # this method will not modify the left and top pixels,
    # but will modify the right (img[:, -1]) and bottom img([-1, :]) pixels
    x = np.linspace(0, img.shape[0] - 1, height + 1)[:-1, np.newaxis]
    x1 = x.astype(int)
    x2 = x1 + 1

    y = np.linspace(0, img.shape[1] - 1, width + 1)[np.newaxis, :-1]
    y1 = y.astype(int)
    y2 = y1 + 1

    q11 = img[x1, y1]
    q21 = img[x2, y1]
    q12 = img[x1, y2]
    q22 = img[x2, y2]

    interpolation = (q11 * ((x2 - x) * (y2 - y)) +
                     q21 * ((x - x1) * (y2 - y)) +
                     q12 * ((x2 - x) * (y - y1)) +
                     q22 * ((x - x1) * (y - y1)))

    if verbose:
        print(f'{img.shape = }',
              f'{x.shape = }', f'{x1.shape = }', f'{x2.shape = }',
              f'{y.shape = }', f'{y1.shape = }', f'{y2.shape = }',
              f'{q11.shape = }', f'{q21.shape = }',
              f'{q12.shape = }', f'{q22.shape = }',
              f'{interpolation.shape = }',
              sep='\n')

    return interpolation


# You are encouraged to test your program in the main function
def main():
    monkey_island = io.imread('monkey_island.jpg')
    fade = fade_gradually(monkey_island)

    cat = io.imread('cat.jpg')
    # cat_png = io.imread('cat.png')

    img = color.rgb2gray(monkey_island)
    resized_img = my_resize(img, 900, 1600)

    io.imshow_collection([fade, image_matting(cat), resized_img], cmap='gray')
    io.show()


if __name__ == "__main__":
    main()
