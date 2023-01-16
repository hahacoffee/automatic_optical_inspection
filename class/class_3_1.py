clc()
import numpy as np
import matplotlib.pyplot as plt
a=1
f0=20
f=np.linspace(-50,50,10000)
F=a*np.sin(np.pi*f*a)/(np.pi*f*a)+a/2*np.sin(np.pi*(f-f0)*a)/(np.pi*(f-f0)*a)+a/2*np.sin(np.pi*(f+f0)*a)/(np.pi*(f+f0)*a)
plt.plot(f,F)
plt.show()