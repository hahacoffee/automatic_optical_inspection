clc()
x1,y1=eval(input("please give x1,y1:"))
x2,y2=eval(input("please give x2,y2:"))
x3,y3=eval(input("please give x3,y3:"))
x4,y4=eval(input("please give x4,y4:"))

x1=float(x1)
x2=float(x2)
x3=float(x3)
x4=float(x4)
y1=float(y1)
y2=float(y2)
y3=float(y3)
y4=float(y4)
a1=x2-x1
a2=x3-x2
if a1==0:
    a1=0.0001
    m12=(y2-y1)/(a1)
    if m12==0:
        m12=10000000000000000000000000
        xx1=((a1)/2)+x1
        yy1=((y2-y1)/2)+y1
    else:
        xx1=((a1)/2)+x1
        yy1=((y2-y1)/2)+y1
else:
    m12=((y2-y1)/(a1))
    if m12==0:
        m12=10000000000000000000000000
        xx1=((a1)/2)+x1
        yy1=((y2-y1)/2)+y1
    else:
        xx1=((a1)/2)+x1
        yy1=((y2-y1)/2)+y1

if a2==0:
    a2=0.0001
    m23=((y3-y2)/(a2))
    if m23==0:
        m23=10000000000000000000000000
        xx2=((a2)/2)+x2
        yy2=((y3-y2)/2)+y2
    else:
        xx2=((a2)/2)+x2
        yy2=((y3-y2)/2)+y2
else:
    m23=((y3-y2)/(a2))
    if m23==0:
        m23=10000000000000000000000000
        xx2=((a2)/2)+x2
        yy2=((y3-y2)/2)+y2
    else:
        xx2=((a2)/2)+x2
        yy2=((y3-y2)/2)+y2

if m12==m23:
    print("p1,p2 and p3 is not a circle")
else:
    y=(1/(m12-m23))*((m12*yy1)-(m23*yy2)+xx1-xx2)
    x=((yy1-y)*m12)+xx1

    dis1=(x1-x)**2+(y1-y)**2
    dis2=(x2-x)**2+(y2-y)**2
    dis3=(x3-x)**2+(y3-y)**2
    dis4=(x4-x)**2+(y4-y)**2

    if dis1>dis2:
        disr=dis1
    else:
        disr=dis2
    if disr>dis3:
        disr=disr
    else:
        disr=dis3
    if disr>dis4:
        print("point is in the circle")
    else:
        print("point is NOT in the circle")
