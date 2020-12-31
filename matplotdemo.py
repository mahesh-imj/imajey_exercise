import matplotlib.pyplot as plt
import math
for t in range(0,5):
  x=[i for i in range(-3,4)]
  #using map function with lambda may help  
  y=[float((math.e**t)*math.sin(i*t)+(i**2)) for i in x]
  plt.plot(x,y,label=f"for t= {t} ")
  plt.xlabel('X axis')
  plt.ylabel('Y axis')
  plt.title('Graph for equation y=(e^t)*sin(x*t)+(x^2)')
  plt.legend()
  plt.show()
