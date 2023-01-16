clc()
s=dataObject()
filter("loadAnyImage",s,'3grating.jpg') 
X0=1 
Y0=1
D0=1 
N=1000 
dx=X0/N 
dy=Y0/N 
dfx=D0/N 
s.setAxisScale(1,dx)
s.setAxisScale(0,dy)
S=s[1,:]
d=dataObject()
filter("fftw",S, d) 
filter("fftshift",d) 
d.setAxisScale(1,dfx)
plot(d)