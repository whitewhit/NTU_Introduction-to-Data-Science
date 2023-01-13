import numpy as np
import matplotlib.pyplot as plt

from skimage import io, filters
from scipy.signal import convolve2d

# (a)
filter_a = np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]])

# (b)
filter_b = np.array([[-1, -1, 2], [-1, 2, -1], [2, -1, -1]])

# (c)
filter_c = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# (e)
filter_e = np.array([[0, -1, 0], [1, 0, 1], [0, -1, 0]])

def main():
    yellow_fan = io.imread('building.jpg', as_gray=True)

    yellow_fan_a = convolve2d(yellow_fan, filter_a, mode='same')

    yellow_fan_b = convolve2d(yellow_fan, filter_b, mode='same')

    yellow_fan_c = convolve2d(yellow_fan, filter_c, mode='same')

    yellow_fan_d = filters.sobel_v(yellow_fan)

    yellow_fan_e = convolve2d(yellow_fan, filter_e, mode='same')


    plt.figure(figsize=(20, 4))
    plt.subplot(1, 5, 1)
    plt.title('a')
    plt.imshow(yellow_fan_a, cmap='gray',  vmin=-0.5, vmax=1)

    plt.subplot(1, 5, 2)
    plt.title('b')
    plt.imshow(yellow_fan_b, cmap='gray',  vmin=-0.5, vmax=1)

    plt.subplot(1, 5, 3)
    plt.title('c')
    plt.imshow(yellow_fan_c, cmap='gray',  vmin=-0.5, vmax=1)

    plt.subplot(1, 5, 4)
    plt.title('d')
    plt.imshow(yellow_fan_d, cmap='gray',  vmin=-0.5, vmax=1)

    plt.subplot(1, 5, 5)
    plt.title('e')
    plt.imshow(yellow_fan_e, cmap='gray',  vmin=-0.5, vmax=1)
  
    plt.show()

if __name__ == "__main__":
    main()