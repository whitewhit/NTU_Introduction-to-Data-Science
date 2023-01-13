import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

df = pd.read_excel("Scatter.xlsx")
pc1 = df["PC1"]
pc2 = df["PC2"]
genotype = df["Genotype"]

pc1_0 = []
pc1_1 = []
pc1_2 = []

pc2_0 = []
pc2_1 = []
pc2_2 = []

for i in range(0, len(genotype)):
    if genotype[i] == 0:
        pc1_0.append(pc1[i])
        pc2_0.append(pc2[i])
    if genotype[i] == 1:
        pc1_1.append(pc1[i])
        pc2_1.append(pc2[i])
    if genotype[i] == 2:
        pc1_2.append(pc1[i])
        pc2_2.append(pc2[i])

colors = np.array(['#FF93A0', '#FFFF92', '#9DD6FF'])
markers = ['^', 'o', 's']
labels = ['c/c', 'C/c', 'C/C']

fig = plt.figure(figsize=(8,6))

ax = []
gs = fig.add_gridspec(3, 3, hspace=0.7, wspace=1.3)

ax.append(fig.add_subplot(gs[:2, 0]))
ax.append(fig.add_subplot(gs[:2, 1:]))
ax.append(fig.add_subplot(gs[2, 1:]))

for x in ax:
    x.tick_params(axis='both', direction='in', bottom=True, top=True,
                  left=True, right=True)

    x.set_xlim(-400, 400)
    x.set_xticks([-400, -200, 0, 200, 400])
    x.set_xlabel('PC1', fontsize=14)

    x.set_ylim(-400, 400)
    x.set_yticks([-400, -200, 0, 200, 400])
    x.set_ylabel('PC2',  fontsize=14)

ax[1].set_title('Scatter Plot', fontsize=14)

x = ax[0]
x.set_xlim(0, 10)
x.set_xticks([0, 5, 10])
x.set_xlabel('Frequency', fontsize=14)

x = ax[2]
x.set_ylim(0, 10)
x.set_yticks([0, 5, 10])
x.set_ylabel('Frequency', fontsize=14)

# 左上的圖
ax[0].hist([pc2_0, pc2_1, pc2_2],
            histtype='barstacked',
            orientation='horizontal', 
            rwidth=0.8, 
            color=colors, 
            edgecolor='k',
            zorder=10) 

# 右下的圖
ax[2].hist([pc1_0, pc1_1, pc1_2],
            histtype='barstacked',
            orientation='vertical', 
            rwidth=0.8, 
            color=colors, 
            edgecolor='k',
            zorder=10) 

# 右上的圖
x = ax[1]
legend_elements = []

x.scatter(pc1_0, pc2_0, color=colors[0], marker=markers[0], edgecolor='k')
x.scatter(pc1_1, pc2_1, color=colors[1], marker=markers[1], edgecolor='k')
x.scatter(pc1_2, pc2_2, color=colors[2], marker=markers[2], edgecolor='k')

for i in range(0, 3):
    legend_elements.append(Line2D([0], [0], c=colors[i], lw=0, marker=markers[i], ms=12,
                            mec='k', mew=1, label=labels[i]))

# 右下的圖
x = fig.add_subplot(gs[-1, 0])
x.tick_params(labelcolor='none', which='both', bottom=True, top=True,
              left=True, right=True)
x.set_xlim([0, 1])
x.set_xticks([0, 1])
x.set_ylim([0, 1])
x.set_yticks([0, 1])
x.legend(handles=legend_elements, loc='center',  frameon=False)

plt.show()