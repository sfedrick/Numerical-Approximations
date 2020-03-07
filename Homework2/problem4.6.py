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
	v=T*np.e**(-t)+c*e**(-3-3*t)*T
	return v

def f(y,t):
	alpha=(3*t)/(1+t)
	beta=2*((1+t)**3)*np.e**(-t)
	dydt=-alpha*y+beta
	return dydt
Et,Ey=eulerE(1,0,15,f,0.2)
Et1,Ey1=eulerE(1,0,15,f,0.8)
Et2,Ey2=eulerE(1,0,15,f,1.1)
t1,y1=eulerI(1,0,15,0.2)
#plot results

figure=plt.figure()
ax=figure.add_subplot()
ax.plot(Et,Ey)
ax.plot(Et1,Ey1)
ax.plot(Et2,Ey2)
ax.set_xlabel("Y(t)")
ax.set_ylabel(r"$Time$")
figure.suptitle("Explicit Euler")
figure1=plt.figure()
ax1=figure1.add_subplot()
ax1.plot(t1,y1)
ax1.set_xlabel("Y(t)")
ax1.set_ylabel(r"$Time$")
figure1.suptitle("Implicit Euler")
plt.show()
