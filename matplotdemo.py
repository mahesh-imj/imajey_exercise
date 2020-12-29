import matplotlib.plot as plt
from math import *
for t in range(0,3):
   for x in range(-3,3):
      y=(math.e^t)*math.sin(x*t)+(x*x)
      plt.plot(x,y)
      plt.show()
