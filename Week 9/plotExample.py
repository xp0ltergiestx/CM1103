import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(221) #221 -> top left
ax1.plot([1,2,3,4,5], [10,5,10,5,10], 'ro')

ax2 = fig.add_subplot(222) #222 -> top right
ax2.plot([1,2,3,4], [1,4,9,16], 'kx')

ax3 = fig.add_subplot(223) #223 -> bottom left
ax3.plot([1,2,3,4], [1,10,100,1000], 'b+')

ax4 = fig.add_subplot(224) #224 -> bottom right
ax4.plot([1,2,3,4], [0,0,1,1], 'g-')

plt.show()

