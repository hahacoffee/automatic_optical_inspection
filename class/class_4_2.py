clc()
fig=figure(1,rows=1,cols=2)
s=dataObject()
filter("loadAnyImage",s,"2dgratingAperture.jpg")
L=1 # mm
Nx,Ny=s.shape
dx=L/Nx
dy=L/Ny
s.setAxisScale(1,dx)
s.setAxisScale(0,dy)
fig.plot(s,areaIndex=0)
df=1/L #??????????????:setAxisScale()?????????????
d=dataObject()
filter("fftw2D",s,d)
filter("fftshift",d)
fig.plot(d,areaIndex=1,properties={"colorMap":"falseColor"})