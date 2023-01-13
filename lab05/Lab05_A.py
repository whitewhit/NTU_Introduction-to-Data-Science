import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

month = df['month_number']
bathingsoap = df['bathingsoap']
facewash = df['facewash']

fig, axes = plt.subplots(nrows = 2, ncols = 1, sharex=True, figsize=(8, 4), dpi=100)
fig.supylabel("Sales units in number", fontsize=14)


#第一張子圖
axes1 = axes[0]
axes1.plot(month, bathingsoap, '-ok')
axes1.set_title("Sales data of a Bathingsoap", fontsize=14)
axes1.set_yticks([7500, 10000, 12500])

#第二張子圖

axes2 = axes[1]
axes2.plot(month, facewash, '-ok')
axes2.set_title("Sales data of a facewash", fontsize=14)

axes2.set_xticks(month)
axes2.set_yticks([1500, 2000])
axes2.set_xlabel("Month Number",fontsize=14)

plt.subplots_adjust(hspace=0.4)
plt.show()