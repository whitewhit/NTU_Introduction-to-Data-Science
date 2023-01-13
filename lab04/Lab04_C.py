import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0., 4*np.pi, 250)
y = np.sin(x) + np.sin(3*x)
y_stick = [-1, -0.3, 0.1, 1]

labels = ['Minimnm', 'Critical', 'Collapse', 'maximum']

plt.plot(x, y, color='#FF00FF', linewidth=2.0)

plt.yticks(y_stick, labels)
# plt.xticks([2, 4, 6, 8, 10, 12, 14], [2, 4, 6, 8, 10, 12, 14], color='#33FF33')
plt.tick_params(axis='x',   
                labelsize='12',   
                color='#33FF33',  
                labelcolor='#33FF33') 

plt.axvline(2, color='#33FF33', linewidth=0.5)
plt.axvline(4, color='#33FF33', linewidth=0.5)
plt.axvline(6, color='#33FF33', linewidth=0.5)
plt.axvline(8, color='#33FF33', linewidth=0.5)
plt.axvline(10, color='#33FF33', linewidth=0.5)
plt.axvline(12, color='#33FF33', linewidth=0.5)

plt.axhline(-1, color='k', linewidth=0.5)
plt.axhline(-0.3, color='k', linewidth=0.5)
plt.axhline(0.1, color='k', linewidth=0.5)
plt.axhline(1, color='k', linewidth=0.5)

plt.xlim(0, 14)
plt.xlabel("x-axis", fontsize=14, color='#33FF33') # x label

plt.show()