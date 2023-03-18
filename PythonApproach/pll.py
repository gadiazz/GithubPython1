import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

plt.style.use('ggplot')
#====================================
figure = pyplot.figure()
ax = plt.axes(projection='3d')
#====================================
xdata = []
ydata =[]
zdata = []
ax.scatter([1,2,3,4],[1,2,3,4],[1,2,3,4],color='red')
plt.show()