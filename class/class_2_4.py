#ITOM????
clc()
src=dataObject()
filter("loadAnyImage",src,'PIC.jpg') 
out=dataObject()
filter("cvSplitChannels",src, out)
r=out[0,:,:]
g=out[1,:,:]
b=out[2,:,:]