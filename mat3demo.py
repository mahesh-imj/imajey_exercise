from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import math
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
x=[i for i in range(-3,4)]
z=t=[j for j in range(0,28,4)]
y=[float((math.e**t)*math.sin(i*t)+(i**2)) for i in x]
ax.plot_wireframe(x,y,z)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis \n y=(e^t)*sin(x*t) + x^2')
ax.set_zlabel(f'Z axis \n t={z}')
plt.title('Graph for equation y=(e^t)*sin(x*t)+(x^2)')
plt.legend()
plt.show()
