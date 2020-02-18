# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:28:33 2020

@author: shaun
"""
from integration import *
import matplotlib.pyplot as plt
from sympy import *

def actualfunction(x):
    a=10**(3.0/2.0)
    b=(10**(0.5))*(10.0*x-3.0)
    c=2*((10.0*x)+1)**(0.5)
    f=a*(np.arctan(b)+c)-(np.pi)*x
    return float(f)

a=0
b=1
actual=actualfunction(b)-actualfunction(a)
trap=[]
trap_error=[]
trapend=[]
trapend_error=[]
simpson=[]
simpson_error=[]
n=[]
for i in range(3,15):
    n.append(2**(i))

for binx in n:
    trap.append(twhole(binx,a,b)[2])
    trapend.append(twhole2(binx,a,b)[2])
    simpson.append(swhole(binx,a,b)[2])
    te=(((actual-trap[-1])**2)**0.5)/actual
    tee=(((actual-trapend[-1])**2)**0.5)/actual
    se=(((actual-simpson[-1])**2)**0.5)/actual
    trap_error.append(te)
    trapend_error.append(tee)
    simpson_error.append(se)
figure1=plt.figure()
figure1.suptitle("Error of each integral method")
ax=figure1.add_subplot(1,1,1)
ax.set_xlabel("N number of bins")
ax.set_ylabel(r"Error")
ax.set_xscale('log')
ax.set_yscale('log')
ax.plot(n,trapend_error,marker='o',label="Trapezoidal with End correction Rule ")
ax.plot(n,simpson_error,marker='x',label="Simpson Rule ")
ax.plot(n,trap_error,marker='^',label="Trapezoidal Rule ")
ax.legend(loc='upperleft')




ans=rhombergwhole(0,1,1000,0.1)
figure2=plt.figure()
figure2.suptitle("Adaptive quad technique romberg integration")
ax=figure2.add_subplot(2,1,1)
ax.plot(ans[0],ans[1])
ax.set_xlabel("X")
ax.set_ylabel(r"$F(X)$")
ax=figure2.add_subplot(2,1,2)
ax.plot(ans[0],ans[2])
ax.set_xlabel("X")
ax.set_ylabel("Number of Evaluations")
