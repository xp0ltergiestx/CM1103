import matplotlib.pyplot as plt
import numpy as np
import pylab
examMarks = [25, 72, 83, 91, 61]
cwkMarks = [56, 90, 45, 62, 60]
plt.plot(examMarks, cwkMarks, 'bx')
plt.axis([0, 100, 0, 100])
plt.ylabel('Coursework Marks')
plt.xlabel('Exam Marks')
plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111)

# x = np.linspace(0, 20, 1000)
# y1 = np.sin(x)
# y2 = np.cos(x)
# pylab.plot(x, y1, '-b', label='sine')
# pylab.plot(x, y2, '-r', label='cosine')
# pylab.legend(loc='upper left')
# pylab.ylim(-1.5, 2.0)
# pylab.show()
