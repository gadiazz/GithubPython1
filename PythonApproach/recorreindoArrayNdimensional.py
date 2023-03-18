import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
fig.gca()
ax = fig.add_subplot(projection='3d')

scale = 0.01


B = np.random.rand(int(480*scale),int(640*scale))
print("Matriz B ","Dimension: ",B.ndim,"Size: ", B.size,"Shape: ", B.shape ,"Matriz: ",B,"\n Vstack: ", np.vstack(B) )
for i in range(0, len(B)):
    #print("Dim No°: ", i , B[i])
    for i2 in range(0, len(B[i])):
        #print("Pixel: ", B[i][i2])
        fig.gca()
        ax.scatter(B[i][i2], B[i][i2], B[i][i2], marker='o')
        
        
        
    


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

