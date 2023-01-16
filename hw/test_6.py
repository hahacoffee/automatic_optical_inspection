import numpy as np
import matplotlib.pyplot as plt
#???????????y'=-2*y-9.8*t+70.7
delt=0.01
vy=100*np.sin(45/180*np.pi)
vx=vy
x=0
y=0
times=0
while 1:
    times=times+1
    plt.plot(x,y)
    ydel=y+delt*(-2*y-9.8*times+70.7)
    xdel=x+delt*(2*x+70.7)
    if ydel<y:
        break
    x=xdel
    y=ydel