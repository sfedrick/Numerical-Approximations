# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:24:13 2020

@author: shaun
"""
import numpy as np
import matplotlib.pyplot as plt
from odesolvers import *
def fexact(t):
	c=0
	T=(1+t)**3
	v=T*np.e**(-t)+c*np.e**(-3-3*t)*T
	return v

def f(y,t):
	alpha=(3*t)/(1+t)
	beta=2*((1+t)**3)*np.e**(-t)
	dydt=-alpha*y+beta
	return dydt
x=np.linspace(0,15,100)
y=fexact(x)
Et,Ey=eulerE(1,0,15,f,0.2)
Et1,Ey1=eulerE(1,0,15,f,0.8)
Et2,Ey2=eulerE(1,0,15,f,1.1)

EIt,EIy=eulerI(1,0,15,0.2)
EIt1,EIy1=eulerI(1,0,15,0.8)
EIt2,EIy2=eulerI(1,0,15,1.1)

Rt,Ry=rk4(1,0,15,f,0.2)
Rt1,Ry1=rk4(1,0,15,f,0.8)
Rt2,Ry2=rk4(1,0,15,f,1.1)
#plot results

R2t,R2y=rk2(1,0,15,f,0.2)
R2t1,R2y1=rk2(1,0,15,f,0.8)
R2t2,R2y2=rk2(1,0,15,f,1.1)

tt,ty=eulerT(1,0,15,0.2)
tt1,ty1=eulerT(1,0,15,0.8)
tt2,ty2=eulerT(1,0,15,1.1)

figure=plt.figure()
ax=figure.add_subplot()
ax.plot(x,y,label="Exact solution")
ax.plot(Et,Ey,label="h=0.2")
ax.plot(Et1,Ey1,label="h=0.8")
ax.plot(Et2,Ey2,label="h=1.1")
ax.set_xlabel("Y(t)")
ax.set_ylabel(r"$Time$")
ax.set_ylim(bottom=-1, top=6)
figure.suptitle("Explicit Euler")
ax.legend()
figure1=plt.figure()
ax1=figure1.add_subplot()
ax1.plot(x,y,label="Exact solution")
ax1.plot(EIt,EIy,label="h=0.2")
ax1.plot(EIt1,EIy1,label="h=0.8")
ax1.plot(EIt2,EIy2,label="h=1.1")
ax1.set_xlabel("Y(t)")
ax1.set_ylabel(r"$Time$")
figure1.suptitle("Implicit Euler")
ax1.legend()

figure2=plt.figure()
ax2=figure2.add_subplot()
ax2.plot(x,y,label="Exact solution")
ax2.plot(Rt,Ry,label="h=0.2")
ax2.plot(Rt1,Ry1,label="h=0.8")
ax2.plot(Rt2,Ry2,label="h=1.1")
ax2.set_xlabel("Y(t)")
ax2.set_ylabel(r"$Time$")
figure2.suptitle("Runge Kuta 4th order")
ax2.legend()


figure3=plt.figure()
ax3=figure3.add_subplot()
ax3.plot(x,y,label="Exact solution")
ax3.plot(R2t,R2y,label="h=0.2")
ax3.plot(R2t1,R2y1,label="h=0.8")
ax3.plot(R2t2,R2y2,label="h=1.1")
ax3.set_xlabel("Y(t)")
ax3.set_ylabel(r"$Time$")
ax3.set_ylim(bottom=-1, top=6)
figure3.suptitle("Runge Kuta 2nd order")
ax3.legend()


figure4=plt.figure()
ax4=figure4.add_subplot()
ax4.plot(x,y,label="Exact solution")
ax4.plot(tt,ty,label="h=0.2")
ax4.plot(tt1,ty1,label="h=0.8")
ax4.plot(tt2,ty2,label="h=1.1")
ax4.set_xlabel("Y(t)")
ax4.set_ylabel(r"$Time$")
ax4.set_ylim(bottom=-1, top=6)
figure4.suptitle("Trapezoidal")
ax4.legend()
plt.show()
