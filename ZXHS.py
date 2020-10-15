import numpy as np
import matplotlib.pyplot as plt
import math

x=np.arange(-20,3*np.pi,0.02)
y=np.sin(x+math.pi)

plt.xlabel('                                                                          t')
plt.ylabel('x(t)=Asin(ωt+φ)')


plt.plot(x,y)
plt.show()