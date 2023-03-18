import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import numpy as np
from random import randint
#============================================================================================
plt.style.use('ggplot')
#============================================================================================
xdata = []
ydata =[]
zdata = []
scale = 1
#============================================================================================
figure = pyplot.figure()
ax = plt.axes(projection='3d')
#ax.scatter(xdata,ydata,zdata,'o',color='red')
#============================================================================================
def update(frame):
    xdata.append(np.random.rand(4))
    ydata.append(np.random.rand(4))
    zdata.append(np.random.rand(4))
    ax.set_animated(True)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return ax
#============================================================================================


if __name__ == '__main__':
    animacion3D = FuncAnimation(figure,update,cache_frame_data=True)
    plt.show()