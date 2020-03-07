import numpy as np
import matplotlib.pyplot as plt
from odesolvers import *
h=50
hEE=h
hT=3*h
hf=h
hr4=4*h
hr2=2*h
w=1
def AerrorEE(m):
    T=50
    hEE=(T)/m
    error=(1+(w*hEE)**2)**(0.5)
    return error

def Ark2error(m):
    T=50
    hr2=(T*2)/m
    error=(1+((w*hr2)**4)/4)**(0.5)
    return error
def Ark4error(m):
    T=50
    hr4=(T*4)/m
    error=((((hr4**8)*(w**8))-8*((hr4**6)*(w**6))+588)**0.5)/24
    return error
def ATerror(m):
    return 0
def Alferror(m):
     return 0

def amperror(mlist,s,e):
    y=[]
    for m in mlist:
        yn=1-abs(s(m))**(m/e)
        y.append(yn)
    y=np.array(y)
    return y
def PerrorEE(m):
    T=50
    hee=(T)/m
    error=w*(hEE**3)*m
    return error

def Prk2error(m):
    T=50
    hr2=(T*2)/m
    error=-w*((hr2**3)/6)*(m/2)
    return error
def Prk4error(m):
    T=50
    hr4=(T*4)/m
    error=-w*((hr2**5)/120)*(m/4)
    return error
def PTerror(m):
    T=50
    h=(T*3)/m
    error=w*((h**3)/12)*(m/3)
    return error
def Plferror(m):
    T=50
    h=(T)/m
    error=-w*((h**3)/6)*(m)
    return error
def phaerror(mlist,s,e):
    y=[]
    for m in mlist:
        yn=s(m)
        y.append(yn)
    y=np.array(y)
    return y
M=np.linspace(100,1000)
Ark2=abs(amperror(M,Ark2error,2))
Ark4=abs(amperror(M,Ark4error,4))
AEE=abs(amperror(M,AerrorEE,1))

Prk2=abs(phaerror(M,Prk2error,2))
Prk4=abs(phaerror(M,Prk4error,2))
PEE=abs(phaerror(M,PerrorEE,2))
Plf=abs(phaerror(M,Plferror,2))
PT=abs(phaerror(M,PTerror,2))

figureA=plt.figure()
ax=figureA.add_subplot()
ax.loglog(M,AEE,label="Explicit Euler")
ax.loglog(M,Ark2,label="Runge Kutta second order")
ax.loglog(M,Ark4,label="Runge Kutta fourth order")
ax.legend()
ax.set_xlabel("M")
ax.set_ylabel(r"Amplitude error")
ax.set_title("Amplitude error")
figureA.suptitle("Amplitude Error for various methods")

figureB=plt.figure()
ax2=figureB.add_subplot()
ax2.loglog(M,Prk2,label="Runge Kutta second order")
ax2.loglog(M,Prk4,label="Runge Kutta fourth order")
ax2.loglog(M,PEE,label="Explicit Euler")
ax2.loglog(M,Plf,label="Leap Frog")
ax2.loglog(M,PT,label="Trapezoidal")
ax2.set_title("Phase error")
ax2.set_ylabel(r"Phase error")
ax2.set_xlabel("M")
ax2.legend()

plt.show()
