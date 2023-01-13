import math
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io, color


# Do NOT modifify the function names

def my_resize(img, height, width):
    
    img = skimage.img_as_float(img)

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

    return interpolation, height, width


def my_rotation(img, angle):

    # img_rotation = transform_matrix * img_copy
    rads = angle*np.pi/180
    
    # Let us find the height and width of the rotated img
    height_rot_img = round(abs(img.shape[0]*math.cos(rads))) + \
                       round(abs(img.shape[1]*math.sin(rads)))
    width_rot_img = round(abs(img.shape[1]*math.cos(rads))) + \
                       round(abs(img.shape[0]*math.sin(rads)))

    # color
    if np.ndim(img) == 3:
        rot_img = np.uint8(np.zeros((height_rot_img,width_rot_img,img.shape[2])))
    # grayscale
    elif np.ndim(img) == 2:
        rot_img = np.uint8(np.zeros((height_rot_img,width_rot_img)))
        rot_img = skimage.img_as_float(rot_img)

    # Finding the center point of the original img
    cx, cy = (img.shape[1]//2, img.shape[0]//2)

    # Finding the center point of rotated img.
    midx, midy = (width_rot_img//2, height_rot_img//2)
     
    for i in range(rot_img.shape[0]):
        for j in range(rot_img.shape[1]):
            x = (i-midx)*math.cos(rads)+(j-midy)*math.sin(rads)
            y = -(i-midx)*math.sin(rads)+(j-midy)*math.cos(rads)

            x = round(x) + cy
            y = round(y) + cx

            if (x>=0 and y>=0 and x<img.shape[0] and  y<img.shape[1]):
                if np.ndim(img) == 3:
                    rot_img[i,j,:] = img[x,y,:]
                elif np.ndim(img) == 2:
                    rot_img[i,j] = img[x,y]

    return rot_img, angle


# You are incouraged to test your program in the main function

def main():

    monkey_island = io.imread('monkey_island.jpg')
    monkey_island_gray = color.rgb2gray(monkey_island)

    resized_img, height, width = my_resize(monkey_island_gray, 1200, 1200)
    
    rotation, angle = my_rotation(monkey_island_gray, 45)

    # resize
    plt.subplot(1, 2, 1)
    plt.title(f"resize height={height} and width={width} ")
    plt.imshow(resized_img, cmap='gray')

    # rotation
    plt.subplot(1, 2, 2)
    plt.title(f"rotation {angle}°")
    # color 
    if np.ndim(rotation) == 3:
        plt.imshow(rotation)
    # grayscale
    elif np.ndim(rotation) == 2:
        plt.imshow(rotation, cmap='gray')

    plt.subplots_adjust(wspace=0.5)
    plt.show()
    
if __name__ == "__main__":
    main()


