import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

labels = ['Cluster 0', 'Cluster 1',  'Cluster 2', 'Center of cluster 0 ', 'Center of cluster 1 ', 'Center of cluster 2']

attack = df["Attack"]
defense = df["Defense"]
cluster = df["cluster"]


attack_0 = []
defense_0 = []
attack_1 = []
defense_1 = []
attack_2 = []
defense_2 = []

for i in range(0, cluster.size):
    if cluster[i] == 0: 
        attack_0.append(attack[i])
        defense_0.append(defense[i])
    elif cluster[i] == 1:
        attack_1.append(attack[i])
        defense_1.append(defense[i])
    elif cluster[i] == 2:
        attack_2.append(attack[i])
        defense_2.append(defense[i])
        

plt.figure(figsize=(9,8)) 

plt.title("Scatter plot of pokemons",  fontsize=16)
plt.xlabel('Attack', fontsize=14)
plt.ylabel('Defense', fontsize=14)

# plt.axis([0., 180., 0., 200.])

plt.scatter(attack_0, 
            defense_0,
            c = 'm',
            s = 10,
            alpha= .3)

plt.scatter(attack_1, 
            defense_1,
            c = 'g',
            s = 10,
            alpha= .3)

plt.scatter(attack_2, 
            defense_2,
            c = 'c',
            s = 10,
            alpha= .3)

plt.scatter(49.875000, 
            48.075000,
            c = 'm',
            s = 100,
            marker='^')

plt.scatter(79.801887, 
            74.386792,
            c = 'g',
            s = 100,
            marker='^')


plt.scatter(112.270833, 
            102.479167,
            c = 'c',
            s = 100,
            marker='^')
            
plt.legend(labels, ncol=2)

plt.show()

