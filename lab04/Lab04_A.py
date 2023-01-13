import matplotlib.pyplot as plt

month = ['Jan', 'Feb', 'March', 'April', 'May', 'June']
sales = [13, 5, 7, 14, 10, 12]

plt.plot(month, sales, '-oc', markersize=10, markerfacecolor='none',linewidth=2.0)
plt.title("Print Sales for January to June, 2022",  fontsize=16) # title

plt.axis([0, 5, 0, 15])

plt.ylabel("Monthly Sales($1000)",  fontsize=14) 

plt.xlabel("Month", fontsize=14) # x label
plt.show()

