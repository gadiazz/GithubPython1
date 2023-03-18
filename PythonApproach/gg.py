import math
import random

radio = 1  # radio del círculo
cantidad_de_puntos = 1000  # cantidad de puntos que queremos encontrar

angulo = 2 * math.pi / cantidad_de_puntos

x1 = []
y1 = []
z1 = []

for i in range(cantidad_de_puntos):
    x = radio * math.cos(angulo * i)
    y = radio * math.sin(angulo * i)
    z = random.uniform(-radio, radio)

    x1.append(x)
    y1.append(y) 
    z1.append(z)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear una figura en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#Reducir dimension

# Graficar los datos en 3D
ax.scatter(x1, y1, z1, c='r', marker='o')

# Establecer etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la figura
plt.show()  
