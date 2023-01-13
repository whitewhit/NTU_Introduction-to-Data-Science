from skimage import io
import numpy as np
import matplotlib.pyplot as plt


example = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
                    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

example_1 = np.copy(example)

width = example.shape[0]
height = example.shape[0]

for i in range(1, height):
    for j in range(1, width):
        if ((example[i-1,j-1] + example[i-1,j] + example[i,j-1] + example[i,j]) < 4):
            example_1[i, j] = 0

plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1)
plt.title('Before eroded', fontsize=25)
plt.imshow(example, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('After eroded', fontsize=25)
plt.imshow(example_1, cmap='gray')
plt.show()
