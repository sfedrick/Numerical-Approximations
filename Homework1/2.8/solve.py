# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 05:42:59 2020

@author: shaun
"""
from derivatives import *
import matplotlib.pyplot as plt
from sympy import *

def construct(a,b,c,l):
    A=[]
    B=[]
    C=[]
    D=[]
    B.append(b[0])
    C.append(c[0])
    for k in range(0,l-2):
        A.append(a[1])
        B.append(b[1])
        C.append(c[1])
    B.append(b[2]) 
    A.append(a[2])
    T = tridiag(A, B, C)
    T[0,2]=c[2]
    T[-1,-3]=a[0]
    return T
N=1000
x=np.linspace(0,1,N)
h=((x[1]-x[0])**2.0)**0.5
A=construct([0,102.0/25,-11/23],[1,-5/12.0,1],[-11/23,102.0/25,0],N)
B=(1/(h**2))*construct([-12/23.0,1,48/23.0],[-36.0/23,-2,-36.0/23],[48.0/23,1,-12/23],N)

IA=np.linalg.inv(A)
C=np.matmul(IA,B)
C=C+np.identity(N)
y=np.matmul(np.linalg.inv(C),x**3)

figure2=plt.figure()
figure2.suptitle("Solution to differential equation")
ax=figure2.add_subplot(1,1,1)
ax.plot(x,y)
ax.set_xlabel(r"$X$")
ax.set_ylabel(r"$Y$")

