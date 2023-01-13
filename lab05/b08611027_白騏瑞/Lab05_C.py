import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.lines import Line2D

df = pd.read_csv("Score.csv")

colors = np.array(['#9FD959', '#61B0FF', '#FFC000'])
legend_elements = []

fig, ax = plt.subplots(1)
ax.set_title('Points')

ax.spines['left'].set_linewidth(1)
ax.spines['left'].set_zorder(15)

ax.set_xlim([0, 168])
ax.set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 160])
ax.tick_params(axis='x', colors='#7F7F7F')

ax.set_yticks([11, 12, 13, 14, 15])

lefts = pd.DataFrame(df['Round'].unique(), columns=['Round'])
lefts['left'] = 0
for team, color in zip(df['Team'].unique(), colors):
    data = df[df['Team'] == team]
    ax.barh(data['Round'], data['Score'], color=color, ec='w', linewidth=1.2,
            height=0.6, left=lefts.merge(data, on='Round', how='right')['left'],
            zorder=10)
    lefts = lefts.merge(data[['Round', 'Score']], on='Round', how='left')
    lefts['left'] = lefts['left'].add(lefts['Score'], fill_value=0)
    lefts = lefts.drop('Score', axis=1)

    for i, label in zip(range(-len(data), 0), data['Leader']):
        r = ax.patches[i]
        ax.text(r.get_x() + r.get_width() / 2, r.get_y() + r.get_height() / 2,
                label, ha='center', va='center', color='#474C3C', zorder=20)

    legend_elements.append(Line2D([0], [0], c=color, lw=0, marker='s', ms=14,
                                  label=f'Team {team}'))

ax.legend(handles=np.array(legend_elements)[[1, 0, 2]].tolist(),
          loc='lower right', fontsize=9, borderpad=0.8, labelspacing=1.25,
          handlelength=2.1, handletextpad=0.4, borderaxespad=0.85)

plt.show()