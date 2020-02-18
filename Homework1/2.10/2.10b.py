# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:20:23 2020

@author: shaun
"""
import numpy as np
import matplotlib.pyplot as plt
from derivatives import *
plt.ion()
def function(x):
    f=1-(x**8)
    return f
def exact(x):
    f=-8*(x**7)
    return(f)
N=32
j=np.linspace(0,N)
y=(np.pi/N)*j
delta=y[1]-y[0]
a=0.98
X=np.cos(y)

central=[]
x=[]
for i in range(1,len(X)-1):
    cd=(function(X[i+1])-function(X[i-1]))/(2.0*delta)
    central.append(cd)
    x.append(X[i])
central= np.asarray(central)
x=np.asarray(x)
df=(-1/((1-(x**2))**(0.5)))*central
dfexact=[]
for i in x:
    dfexact.append(exact(i))
    
figure=plt.figure()
ax=figure.add_subplot(111)
figure.suptitle("Part b Nonuniform Grid")
ax.plot(x,df,marker='^',label="Nonuniform Grid")
ax.plot(x,dfexact,marker='o',label="Exact solution")
ax.legend(loc='upperleft')
ax.set_xlabel(r"$X$")
ax.set_ylabel(r"$F(x)$")
ax.set_xlim(-0.6,-0.5)
ax.set_ylim(-0.1,0.5)
