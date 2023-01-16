clc()
import numpy as np
fig1=figure(1,rows=4,cols=1)
g0=np.loadtxt("hw0515.txt")

G0=1            # sampling duration
GN=len(g0)   #sampling number
gx0=G0/GN  # time space
GF=1/G0      # frequcy scale
t=g0

t=dataObject(t); t_fft=dataObject()
t.setAxisScale(1,gx0)
filter("fftw",t, t_fft)
filter("fftshift",t_fft)
t_fft.setAxisScale(1,GF)
w=dataObject.zeros([1,GN],dtype='complex128')
w[0,480]=1;w[0,500]=1;w[0,520]=1;                   # frequency=20 Hz
wt=w.mul(t_fft)                                                    #window*spectrum
iwt=dataObject()
filter("ifftw",wt, iwt)

t.setAxisUnit(1,"sec");t_fft.setAxisUnit(1,"Hz");wt.setAxisUnit(1,"Hz");iwt.setAxisUnit(1,"sec");
fig1.plot(t,areaIndex=0)
fig1.plot(t_fft,areaIndex=1,properties={"xAxisInterval":[-500,500]})
fig1.plot(wt,areaIndex=2,properties={"xAxisInterval":[450,550]})
fig1.plot(iwt,areaIndex=3)