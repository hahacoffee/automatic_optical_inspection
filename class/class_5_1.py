clc()
src=dataObject()
filter("loadAnyImage",src,"square.png")
gray=dataObject()
filter("cvCvtColor",src,gray,7)

edge=dataObject()
filter("cvCannyEdge",gray, edge)
fig=figure(rows=1,cols=2)
fig.plot(src,areaIndex=0)
fig.plot(edge,areaIndex=1)