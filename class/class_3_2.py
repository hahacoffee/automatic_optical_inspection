clc()
import numpy as np
fig1=figure(1,rows=2,cols=1)
fig2=figure(2,rows=3,cols=2)
X0=1 #????
N=1000 #???
dx0=X0/N #???? (???????)
F=1/X0 #????
x0=np.linspace(0,X0,N)
fg1=100
fg2=200
t=2+np.cos(2*np.pi*fg1*x0+np.pi)+2*np.cos(2*np.pi*fg2*x0)
A=np.zeros(len(t))
A[500:550]=1
t=t*A

t=dataObject(t)
t_fft=dataObject()

t.setAxisScale(1,dx0) # 0:y??1:x????pixel????
filter("fftw",t,t_fft) 
filter("fftshift",t_fft) 
t_fft.setAxisScale(1,F)
t_fft.setAxisUnit(1,"Hz")
fig1.plot(t,areaIndex=0)
fig1.plot(t_fft,areaIndex=1)
