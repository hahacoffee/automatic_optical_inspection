clc()
import numpy as np
fig=figure(1,rows=3,cols=1)
X0=1 #signal length or sampling duration
N=1000 #sampling number
dx0=X0/N # time space
F=1/X0 # frequcy scale
x0=np.linspace(0,X0,N)
fg1=20;
t=1+np.cos(2*np.pi*fg1*x0)
#A=np.zeros(len(t)); A[300:600]=1;t=t*A
t=dataObject(t)
t.setAxisScale(1,dx0)
t_fft=dataObject()
filter("fftw",t,t_fft)
filter("fftshift",t_fft)
t_fft.setAxisScale(1,F)
t_fft.setAxisUnit(1, "Hz")
t_fft.setAxisDescription(1,"frequency")
fig.plot(t,areaIndex=0)
fig.plot(t_fft,areaIndex=1)
w=dataObject.zeros([1,N],dtype='complex128')
w[0,490]=1;w[0,500]=1;w[0,510]=1#w[0,490:515]=1
wt=w.mul(t_fft)
iwt=dataObject()
filter("ifftw",wt, iwt)
fig.plot(iwt,areaIndex=2)