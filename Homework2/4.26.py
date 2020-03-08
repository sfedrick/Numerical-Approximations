import numpy as np
import matplotlib.pyplot as plt
from odesolversystem import *
def dx(T,t):
    dx=T[1]
    return dx
def dx2(T,x):
    a=-(x+3)/(x+1)
    b=(x+3)/((x+1)**2)
    f=2*(x+1)+3*b
    dx2=-a*T[1]-b*T[0]+f
    return dx2
def alpha(x):

    return A
def Beta(x):
    B=(x+3)/((x+1)**2)
    return B
def Charlie(x):

    return C
def a(x,h,loc):
    A=-(x+3)/(x+1)
    A=(1/(h**2))-(A/(h*2))
    if(loc==1):
        A=A
    elif(loc==0):
        A=A
    elif(loc==-1):
        A=0
    return A
def b(x,h,loc):
    B=(x+3.0)/((x+1.0)**2)
    B=B-(2/(h**2))
    if(loc==1):
        B=1
    elif(loc==0):
        B=B
    elif(loc==-1):
        B=1
    return B
def c(x,h,loc):
    C=-(x+3)/(x+1)
    C=(1/(h**2))+(1/(2.0*h))*C
    if(loc==1):
        C=0
    elif(loc==0):
        C=C
    elif(loc==-1):
        C=C
    return C
def d(x,h,loc):
    b=(x+3.0)/((x+1.0)**2)
    f=2*(x+1)+3*b
    y0=5
    yn=4
    if(loc==1):
        D=y0
    elif(loc==0):
        D=f
    elif(loc==-1):
        D=yn
    return D

xp,tp=direct(a,b,c,d,100,[0,2])


system=[dx,dx2]
g1=[5,1]
g2=[5,-1]


x,t=linshot(g1,g2,2,4,0.02,system)
g1=[5,1]
g2=[5,0]
x1,t1=linshot(g1,g2,2,4,0.2,system)
figure=plt.figure()
ax=figure.add_subplot()
ax.plot(tp,xp,label="Direct Method")
ax.plot(t,x,label="Shooting method")
ax.plot(t1,x1,label="Shooting method init condition 0")
ax.set_xlabel("Length")
ax.set_ylabel("Temperature")
ax.legend()
plt.show()
