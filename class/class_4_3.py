# ??????   +window
clc()
fig=figure(1,rows=2,cols=2)
#areaIndex 0: grating img, 1: fft img, 2: fft +window img, 3 ifft
s=dataObject()
filter("loadAnyImage",s,"2dgratingAperture.jpg")
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
fig.plot(d,areaIndex=1,properties={"xAxisInterval":[-100,100],"yAxisInterval":[-100,100],"colorMap":"falseColor"})

w=dataObject.zeros(d.shape,dtype="complex64")
w[:,480:520]=1
dw=d.mul(w)
fig.plot(dw,areaIndex=2,properties={"xAxisInterval":[-100,100],"yAxisInterval":[-100,100],"colorMap":"falseColor"})
dwi=dataObject()
filter("ifftw2D",dw,dwi)
fig.plot(dwi,areaIndex=3)
