clc()
jumper=0
pointer=0
while jumper==0:
    jumper=0
    pointer=0
    px1,py1=eval(input("px1,py1 :"))
    px2,py2=eval(input("px2,py2 :"))
    pxd1=px1-px2
    pyd1=py1-py2
#...............................................................................................................................................................
    while ((pxd1==0)and(pyd1==0)):
        pxd1=px1-px2
        pyd1=py1-py2
        print("p1 and p2 is the same point,please give p2 again")
        px2,py2=eval(input("px2,py2 :"))
        pxd1=px1-px2
        pyd1=py1-py2
    px3,py3=eval(input("px3,py3 :"))
    pxd2=px2-px3
    pyd2=py2-py3
    pxd3=px3-px1
    pyd3=py3-py1
    while (((pxd2==0)and(pyd2==0))or((pxd3==0)and(pyd3==0))):
        pxd2=px2-px3
        pyd2=py2-py3
        while (pxd2==0)and(pyd2==0):
            print("p2 and p3 is the same point,please give p3 again")
            px3,py3=eval(input("px3,py3 :"))
            pxd2=px2-px3
            pyd2=py2-py3
        pxd3=px3-px1
        pyd3=py3-py1
        while (pxd3==0)and(pyd3==0):
            print("p1 and p3 is the same point,please give p3 again")
            px3,py3=eval(input("px3,py3 :"))
            pxd3=px3-px1
            pyd3=py3-py1
        pxd2=px2-px3
        pyd2=py2-py3
        pxd3=px3-px1
        pyd3=py3-py1
    #...............................................................................................................................................................
    if (px2-px1)==0:
        pointer=1
    else:
        mo12=(py2-py1)/(px2-px1)
        pointer=2
    if pointer==2:
        if (px3-px2)==0:
            jumper=1
        else:
            mo23=(py3-py2)/(px3-px2)
            if mo12==mo23:
                jumper=0
            else:
                jumper=1
    if pointer==1:
        if (px3-px2)==0:
            jumper=0
        else:
            jumper=1

    if jumper==0:
        print("three point are colliner")
        print("please give three new points")
#...............................................................................................................................................................
px4,py4=eval(input("px4,py4 :"))

if px1<px2:
    xmid12=px1+abs((px1-px2))/2
else:
    xmid12=px2+abs((px1-px2))/2
if py1<py2:
    ymid12=py1+abs((py1-py2))/2
else:
    ymid12=py1+abs((py1-py2))/2

if px2<px3:
    xmid23=px2+abs((px2-px3))/2
else:
    xmid23=px3+abs((px2-px3))/2
if py2<py3:
    ymid23=py2+abs((py2-py3))/2
else:
    ymid23=py3+abs((py2-py3))/2

if pxd1==0:
    pcy=ymid12
    if pyd2==0:
        pcx=xmid23
    else:
        m23=(px3-px2)/(py2-py3)
        pcx=(pcy-ymid23+(m23*xmid23))/m23
elif pxd2==0:
    pcy=ymid23
    if pyd1==0:
        pcx=xmid12
    else:
        m12=(px2-px1)/(py1-py2)
        pcx=(pcy-ymid12+(m12*xmid12))/m12
elif pyd1==0:
    pcx=xmid12
    if pxd2==0:
        pcy=ymid23
    else:
        m23=(px3-px2)/(py2-py3)
        pcy=ymid23+m23*(pcx-xmid23)
elif pyd2==0:
    pxx=xmid23
    if pxd1==0:
        pcy=ymid12
    else:
        m12=(px2-px1)/(py1-py2)
        pcy=ymid12+m12*(pcx-xmid12)
else:
    m12=(px2-px1)/(py1-py2)
    m23=(px3-px2)/(py2-py3)
    pcx=(ymid23-ymid12+(m12*xmid12)-(m23*xmid23))/(m12-m23)
    pcy=ymid23+m23*(pcx-xmid23)
dc=(px1-pcx)**2+(py1-pcy)**2
dp4=(px4-pcx)**2+(py4-pcy)**2
if dc>dp4:
    print("point4 is inside the circle")
elif dc==dp4:
    print("point4 is on the circle")
else:
    print("point4 is outside the circle")
