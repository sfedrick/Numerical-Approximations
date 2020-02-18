# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 01:17:11 2020

@author: shaun
"""


from derivatives import *
import numpy as np
import matplotlib.pyplot as plt
plt.ion
def actualfunction(x):
    f=-2*np.cos(2*x)*20*np.sin(20*x)+2*np.cos(2*x)*np.e**(np.sin(2*x))
    return f
def function(x):
    f=np.sin(2*x)*np.cos(20*x)+np.e**(np.sin(2*x))
    return f
test=[np.linspace(0,np.pi,256),np.linspace(0,np.pi,512),np.linspace(0,np.pi,1024),np.linspace(0,np.pi,2048)]
x=[np.linspace(0,np.pi,256),np.linspace(0,np.pi,512),np.linspace(0,np.pi,1024),np.linspace(0,np.pi,2048)]
h=[x[0][1]-x[0][0],x[1][1]-x[1][0],x[2][1]-x[2][0],x[3][1]-x[3][0]]

y=[function(x[0]),\
   function(x[1]),\
   function(x[2]),\
   function(x[3])
   ]
firstorder=[]
secondorder=[]
fourthorder=[]

padee=[]
padep=[]
for i in range(0,4):
    x1,y1=firstorderwhole(test[i],y[i],h[i])
    x1=np.asarray(x1)
    x=actualfunction(x1)
    y1=np.asarray(y1)
    x2,y2=secondorderwhole(test[i].copy(),y[i],h[i])
    x2=np.asarray(x2)
    x2=actualfunction(x2)
    y2=np.asarray(y2)
    x4,y4=fourthorderwhole(test[i].copy(),y[i],h[i])
    x4=np.asarray(x4)
    x4=actualfunction(x4)
    y4=np.asarray(y4)
    firstorder.append((((y1-x1)**2)**0.5)/x1)
    secondorder.append((((y2-x2)**2)**0.5)/x2)
    fourthorder.append((((y4-x4)**2)**0.5)/x4)
    
    row1=[-5.0/(2*h[i]),2/h[i],1/(2*h[i])]
    row2=[3.0/h[i],0,0]
    row3=[5.0/(2*h[i]),-2/h[i],-1/(2*h[i])]
    d=np.array([row1,row2,row3], int)
    d2=np.array([row2,row2,row2], float)
    padee.append(pade([0,1,2],[1,4,1],[2,1,0],d,len(x1),function(x1)))
    padep.append(badpade([0,1,2],[1,4,1],[2,1,0],d,len(x1),function(x1)))

errorfirst=[]
errorsecond=[]
errorfourth=[]
errorpade=[]
errorpadep=[]
for x in firstorder:
    x[x == np.inf] = 0
    errorfirst.append(np.mean(x))
for x in secondorder:
    x[x == np.inf] = 0
    errorsecond.append(np.mean(x))
for x in fourthorder:
    x[x == np.inf] = 0
    errorfourth.append(np.mean(x))
for x in padee:
    i=0
    newy=actualfunction(x[i])
    error=(((x-newy)**2)**0.5)/newy
    errorpade.append(np.mean(error))
for x in padep:
    i=0
    newy=actualfunction(x[i])
    error=(((x-newy)**2)**0.5)/newy
    errorpadep.append(np.mean(error))

figure2=plt.figure()
figure2.suptitle("Order of Differentiation technique")
ax=figure2.add_subplot(1,1,1)
ax.set_xlabel(r"grid spacing $\Delta$")
ax.set_ylabel(r"$Error$")
ax.plot(h,errorfirst,marker='o',label="First order error")
ax.plot(h,errorsecond,marker='x',label="Second Order")
ax.plot(h,errorfourth,marker='^',label="Fourth Order")
ax.plot(h,errorpade,marker='.',label="Regular Pade Function")
ax.plot(h,errorpadep,marker='+',label="Periodic Pade function",)

ax.legend()
plt.show()