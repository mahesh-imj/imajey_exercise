import matplotlib.pyplot as plt
import math
x=[i for i in range(-3,3)]
for t in range(0,3):
  y=[float((math.e^t)*math.sin(i*t)+(i*i)) for i in x]  
  plt.plot(x,y,label=f"for t= {t} ")
  plt.xlabel('X axis')
  plt.ylabel('Y axis')
  plt.title('Graph for equation y=(e^t)*sin(x*t)+(x^2)')
  plt.legend()
  plt.show()
