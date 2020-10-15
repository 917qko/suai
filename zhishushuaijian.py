import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(-3.0,3.0,300)
plt.ylim(0,1)
f=2*np.exp((complex(-0.4,8))*-t)
plt.subplot(221)
plt.plot(t,np.real(f))

plt.xlabel('t')
plt.ylabel('x(t)')

plt.show()