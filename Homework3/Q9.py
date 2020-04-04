from odesolversystem import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#initialize vector
def initvector(a,b,N):
    xinit=[]
    X=np.linspace(a,b,N)
    for x in X:
        if(0<=x and x<=0.2):
            xinit.append(1.0-(10.0*x-1.0)**2)
        else:
            xinit.append(0)
    return xinit
def convection(X,t,i):
    u=0.08
    dx=abs(xspace[0]-xspace[1])
    N=len(X)
    if (i==0):
        y=0
        return y
    elif(0<i and i<N-1):
        y=-u*((X[i+1]-X[i-1])/(2*dx))
        return y
    elif(i==N-1):
        y=-u*((X[N-1]-X[N-2])/(dx))
        return y
def laxwendroof(X,t,i):
    u=0.08
    dx=abs(xspace[0]-xspace[1])
    dt=abs(t1-t2)/Nt
    N=len(X)
    if (i==0):
        y=0
        return y
    elif(0<i and i<N-1):
        a=-u*((X[i+1]-X[i-1])/(2*dx))
        b=(((u**2.0)*(dt))/dx)*(X[i+1]-2.0*X[i]+X[i-1])
        y=a+b
        return y
    elif(i==N-1):
        y=-u*((X[N-1]-X[N-2])/(dx))
        return y
def diffusion(X,t,i):
    u=0.08
    al=0.001
    dx=abs(xspace[0]-xspace[1])
    N=len(X)
    if (i==0):
        y=0
        return y
    elif(0<i and i<N-1):
        a=-u*((X[i+1]-X[i-1])/(2*dx))
        b=al*((X[i+1]-2*X[i]+X[i-1])/(dx**2))
        y=a+b
        return y
    elif(i==N-1):
        y=-u*((X[N-1]-X[N-2])/(dx))
        return y


def delayeddiffusion(X0,X,t,i):
    u=0.08
    al=0.001
    dx=abs(xspace[0]-xspace[1])
    N=len(X)
    if (i==0):
        y=0
        return y
    elif(0<i and i<N-1):
        a=-u*((X[i+1]-X[i-1])/(2*dx))
        b=al*((X0[i+1]-2*X0[i]+X0[i-1])/(dx**2))
        y=a+b
        return y
    elif(i==N-1):
        y=-u*((X[N-1]-X[N-2])/(dx))
        return y
def exact(x,t):
    u=0.08
    if 0<=(x-(u*t)) and (x-(u*t))<=0.2 :
        T=1-(10.0*(x-u*t)-1)**2
        return T
    else:
        T=0
        return T
def twant(want,a,b,Nt):
    dt=abs(b-a)/Nt
    tindex=(want-a)/dt
    tindex=int(tindex)
    return tindex
t1=0
t2=8
Nt1=1000
Nt2=400
x0=initvector(0.0,1.0,100)
xspace=np.linspace(0,1,100)

EE1,eet1=odesysE(x0,t1,t2,Nt1,convection)
EE2,eet2=odesysE(x0,t1,t2,Nt2,convection)
eex1=list(EE1.values())
eex2=list(EE2.values())
eex1=np.array(eex1)
eex2=np.array(eex2)

LF1,eet1=odesysLF(x0,t1,t2,Nt1,convection)
LF2,eet2=odesysLF(x0,t1,t2,Nt2,convection)
lfx1=list(LF1.values())
lfx2=list(LF2.values())
lfx1=np.array(lfx1)
lfx2=np.array(lfx2)

EE1,eet1=odesysE(x0,t1,t2,Nt1,diffusion)
EE2,eet2=odesysE(x0,t1,t2,Nt2,diffusion)
deex1=list(EE1.values())
deex2=list(EE2.values())
deex1=np.array(deex1)
deex2=np.array(deex2)

LF1,eet1=odesysLF(x0,t1,t2,Nt1,diffusion)
LF2,eet2=odesysLF(x0,t1,t2,Nt2,diffusion)
dlfx1=list(LF1.values())
dlfx2=list(LF2.values())
dlfx1=np.array(dlfx1)
dlfx2=np.array(dlfx2)

n1=Nt1*20
n2=Nt2*10
LF1,eet1=odesysLFlag(x0,t1,t2,Nt1,delayeddiffusion)
LF2,eet2=odesysLFlag(x0,t1,t2,Nt2,delayeddiffusion)
dlflx1=list(LF1.values())
dlflx2=list(LF2.values())
dlflx1=np.array(dlfx1)
dlflx2=np.array(dlfx2)
'''
x0=initvector(0.0,1.0,100)
xspace=np.linspace(0,1,100)
Nt1=64
Nt=Nt1
LW1,eet1=odesysE(x0,t1,t2,Nt1,laxwendroof)
Nt2=80
Nt=Nt2
LW2,eet2=odesysE(x0,t1,t2,Nt2,laxwendroof)
lwx1=list(LW1.values())
lwx2=list(LW2.values())
lwx1=np.array(lwx1)
lwx2=np.array(lwx2)
'''





eT8=[]
eT4=[]
eT0=[]
for x in xspace:
    eT8.append(exact(x,8))
for x in xspace:
    eT4.append(exact(x,4))
for x in xspace:
    eT0.append(exact(x,0))

figure=plt.figure()
ax=figure.add_subplot(1,2,1)
ax2=figure.add_subplot(1,2,2)
ax.plot(xspace,eex1[:,twant(8,t1,t2,Nt1)],'-o',label="euler t=8")
ax.plot(xspace,eex1[:,twant(4,t1,t2,Nt1)],'-o',label="euler t=4")
ax.plot(xspace,eex1[:,twant(0,t1,t2,Nt1)],'-o',label="euler t=0")
ax2.plot(xspace,eex2[:,twant(8,t1,t2,Nt2)],'-o',label="euler t=8")
ax2.plot(xspace,eex2[:,twant(4,t1,t2,Nt2)],'-o',label="euler t=4")
ax2.plot(xspace,eex2[:,twant(0,t1,t2,Nt2)],'-o',label="euler t=0")
ax.set_title(r'Explicit Euler with N=1000 $\Delta t$=0.008')
ax.plot(xspace,eT8,label="Exact t=8")
ax.plot(xspace,eT4,label="Exact  t=4")
ax.plot(xspace,eT0,label="Exact t=0")
ax2.plot(xspace,eT8,label="Exact t=8")
ax2.plot(xspace,eT4,label="Exact t=4")
ax2.plot(xspace,eT0,label=" Exact t=0")
ax2.set_title(r'Explicit Euler with N=400 $\Delta t$=0.02')
ax.legend(fontsize=4.5,loc="upper right")
ax2.legend(fontsize=4.5,loc="upper right")

figure2=plt.figure()
ax=figure2.add_subplot(1,2,1)
ax2=figure2.add_subplot(1,2,2)
ax.plot(xspace,lfx1[:,twant(8,t1,t2,Nt1)],'-o',label="Leap Frog t=8")
ax.plot(xspace,lfx1[:,twant(4,t1,t2,Nt1)],'-o',label="Leap Frog t=4")
ax.plot(xspace,lfx1[:,twant(0,t1,t2,Nt1)],'-o',label="Leap Frog t=0")
ax2.plot(xspace,lfx2[:,twant(8,t1,t2,Nt2)],'-o',label="Leap Frog t=8")
ax2.plot(xspace,lfx2[:,twant(4,t1,t2,Nt2)],'-o',label="Leap Frog t=4")
ax2.plot(xspace,lfx2[:,twant(0,t1,t2,Nt2)],'-o',label="Leap Frog t=0")
ax.set_title(r'Explicit Leap Frog with N=1000 $\Delta t$=0.008')
ax.plot(xspace,eT8,label="Exact t=8")
ax.plot(xspace,eT4,label="Exact  t=4")
ax.plot(xspace,eT0,label="Exact t=0")
ax2.plot(xspace,eT8,label="Exact t=8")
ax2.plot(xspace,eT4,label="Exact t=4")
ax2.plot(xspace,eT0,label=" Exact t=0")
ax2.set_title(r'Explicit Leap Frog with N=400 $\Delta t$=0.02')
ax.legend(fontsize=4.5,loc="upper right")
ax2.legend(fontsize=4.5,loc="upper right")
'''
figure3=plt.figure()
ax=figure3.add_subplot(1,2,1)
ax2=figure3.add_subplot(1,2,2)
ax.plot(xspace,lwx1[:,twant(8,t1,t2,Nt1)],'-o',label="LaxWendroof t=8")
ax.plot(xspace,lwx1[:,twant(4,t1,t2,Nt1)],'-o',label="LaxWendroof t=4")
ax.plot(xspace,lwx1[:,twant(0,t1,t2,Nt1)],'-o',label="LaxWendroof t=0")
ax2.plot(xspace,lwx2[:,twant(8,t1,t2,Nt2)],'-o',label="LaxWendroof t=8")
ax2.plot(xspace,lwx2[:,twant(4,t1,t2,Nt2)],'-o',label="LaxWendroof t=4")
ax2.plot(xspace,lwx2[:,twant(0,t1,t2,Nt2)],'-o',label="LaxWendroof t=0")
ax.set_title(r'Explicit LaxWendroof with N=64 $\Delta t$=0.125')
ax.plot(xspace,eT8,label="Exact t=8")
ax.plot(xspace,eT4,label="Exact  t=4")
ax.plot(xspace,eT0,label="Exact t=0")
ax2.plot(xspace,eT8,label="Exact t=8")
ax2.plot(xspace,eT4,label="Exact t=4")
ax2.plot(xspace,eT0,label=" Exact t=0")
ax2.set_title(r'Explicit LaxWendroof with N=80 $\Delta t$=0.01')
ax.legend(fontsize=4.5,loc="upper right")
ax2.legend(fontsize=4.5,loc="upper right")
'''
figure4=plt.figure()
ax=figure4.add_subplot(1,2,1)
ax2=figure4.add_subplot(1,2,2)
ax.plot(xspace,deex1[:,twant(8,t1,t2,Nt1)],'-o',label="euler t=8")
ax.plot(xspace,deex1[:,twant(4,t1,t2,Nt1)],'-o',label="euler t=4")
ax.plot(xspace,deex1[:,twant(0,t1,t2,Nt1)],'-o',label="euler t=0")
ax2.plot(xspace,deex2[:,twant(8,t1,t2,Nt2)],'-o',label="euler t=8")
ax2.plot(xspace,deex2[:,twant(4,t1,t2,Nt2)],'-o',label="euler t=4")
ax2.plot(xspace,deex2[:,twant(0,t1,t2,Nt2)],'-o',label="euler t=0")
ax.set_title(r'Explicit Euler diffusion with N=1000 $\Delta t$=0.008')
ax.plot(xspace,eT8,label="Exact t=8")
ax.plot(xspace,eT4,label="Exact  t=4")
ax.plot(xspace,eT0,label="Exact t=0")
ax2.plot(xspace,eT8,label="Exact t=8")
ax2.plot(xspace,eT4,label="Exact t=4")
ax2.plot(xspace,eT0,label=" Exact t=0")
ax2.set_title(r'Explicit Euler diffusion with N=400 $\Delta t$=0.02')
ax.legend(fontsize=4.5,loc="upper right")
ax2.legend(fontsize=4.5,loc="upper right")

figure5=plt.figure()
ax=figure5.add_subplot(1,2,1)
ax2=figure5.add_subplot(1,2,2)
ax.plot(xspace,dlfx1[:,twant(8,t1,t2,Nt1)],'-o',label="Leap Frog t=8")
ax.plot(xspace,dlfx1[:,twant(4,t1,t2,Nt1)],'-o',label="Leap Frog t=4")
ax.plot(xspace,dlfx1[:,twant(0,t1,t2,Nt1)],'-o',label="Leap Frog t=0")
ax2.plot(xspace,dlfx2[:,twant(8,t1,t2,Nt2)],'-o',label="Leap Frog t=8")
ax2.plot(xspace,dlfx2[:,twant(4,t1,t2,Nt2)],'-o',label="Leap Frog t=4")
ax2.plot(xspace,dlfx2[:,twant(0,t1,t2,Nt2)],'-o',label="Leap Frog t=0")
ax.set_title(r'Leap Frog diffusion $\Delta t$=0.008')
ax.plot(xspace,eT8,label="Exact t=8")
ax.plot(xspace,eT4,label="Exact  t=4")
ax.plot(xspace,eT0,label="Exact t=0")
ax2.plot(xspace,eT8,label="Exact t=8")
ax2.plot(xspace,eT4,label="Exact t=4")
ax2.plot(xspace,eT0,label=" Exact t=0")
ax2.set_title(r'Explicit Leap Frog diffusion with N=800 $\Delta t$=0.04')
ax.legend(fontsize=4.5,loc="upper right")
ax2.legend(fontsize=4.5,loc="upper right")


figure6=plt.figure()
ax=figure6.add_subplot(1,2,1)
ax2=figure6.add_subplot(1,2,2)
ax.plot(xspace,dlflx1[:,twant(8,t1,t2,Nt1)],'-o',label="Leap Frog t=8")
ax.plot(xspace,dlflx1[:,twant(4,t1,t2,Nt1)],'-o',label="Leap Frog t=4")
ax.plot(xspace,dlflx1[:,twant(0,t1,t2,Nt1)],'-o',label="Leap Frog t=0")
ax2.plot(xspace,dlflx2[:,twant(8,t1,t2,Nt2)],'-o',label="Leap Frog t=8")
ax2.plot(xspace,dlflx2[:,twant(4,t1,t2,Nt2)],'-o',label="Leap Frog t=4")
ax2.plot(xspace,dlflx2[:,twant(0,t1,t2,Nt2)],'-o',label="Leap Frog t=0")
ax.set_title(r' Leap Frog diffusion lag $\Delta t$=0.02')
ax.plot(xspace,eT8,label="Exact t=8")
ax.plot(xspace,eT4,label="Exact  t=4")
ax.plot(xspace,eT0,label="Exact t=0")
ax2.plot(xspace,eT8,label="Exact t=8")
ax2.plot(xspace,eT4,label="Exact t=4")
ax2.plot(xspace,eT0,label=" Exact t=0")
ax2.set_title(r' Leap Frog diffusion with lag with $\Delta t$=0.08')
ax.legend(fontsize=4.5,loc="upper right")
ax2.legend(fontsize=4.5,loc="upper right")

plt.show()
