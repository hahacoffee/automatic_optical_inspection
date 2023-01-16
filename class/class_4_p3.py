#???
clc()
import numpy as np
fig=figure(1,rows=2,cols=2)
#areaIndex 0: grating img, 1: fft img, 2: fft +window img, 3 ifft
s=dataObject()
filter("loadAnyImage",s,"2Dgrating2.jpg")
L=1 # mm
Nx,Ny=s.shape
dx=L/Nx
dy=L/Ny
s.setAxisScale(1,dx)
s.setAxisScale(0,dy)
fig.plot(s,areaIndex=0)
d=dataObject()
filter("fftw2D",s,d)
filter("fftshift",d)
fig.plot(d,areaIndex=1,properties={"xAxisInterval":[-50,50],"yAxisInterval":[-50,50],"colorMap":"falseColor"})

w=dataObject.zeros(d.shape,dtype="complex64")
q=45*np.pi/180 # ??(??)
c=np.cos(q)
s=np.sin(q)
q1=45*np.pi/180
c1=np.cos(q1)
s1=np.sin(q1)
for i in range(0,15):
    for j in range(0,100):
        a=(465+j*c1)+i*c
        b=(525-j*s1)+i*s
        a=round(a)
        b=round(b)
        a=int(a)
        b=int(b)
        w[a,b]=1

dw=d.mul(w)
fig.plot(dw,areaIndex=2,properties={"xAxisInterval":[-50,50],"yAxisInterval":[-50,50],"colorMap":"falseColor"})
dwi=dataObject()
filter("ifftw2D",dw,dwi)
fig.plot(dwi,areaIndex=3)