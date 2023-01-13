import matplotlib.pyplot as plt
import numpy as np

f = 5000000.
x = np.linspace(0, 0.5, 50)
y = np.sin(2.*np.pi*f*x/1000000)
z = np.cos(2.*np.pi*f*x/1000000)

plt.plot(x, y, '-*c')
plt.plot(x, z, '-ok', markerfacecolor='none')

plt.axis([0, 0.5, -1.5, 1.5])
plt.title("In-Phase (solid) and Quadrature (dotted) Signals",  fontsize=14) # title
plt.ylabel("'Normalized' Signals",  fontsize=14, style='italic') # y label
plt.xlabel("Times(us)", fontsize=14) # x label

plt.annotate('', xy=(0.2, 1.1), xytext=(0.25, 1.1),arrowprops=dict(arrowstyle= " <-> "))
plt.text(0.17, 1.2, 'pi/2 phase lag')

plt.show()