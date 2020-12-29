import matplotlib.plot as plt
from math import *
for t in range(0,3):
   for x in range(-3,3):
      for y=float((math.e^t)*math.sin(x*t)+(x*x)):
         plt.plot(x,y, label='for t='t)
         plt.xlabel('X axis')
         plt.ylabel('Y axis')
         plt.title('Graph for equation y=(e^t)*sin(x*t)+(x^2)')
         plt.legend()
         plt.show()
