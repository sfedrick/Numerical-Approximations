import numpy as np
import pandas as pd
from multipdesys import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import random

def function1(X,grid,input,delta):
    u=input[0]
    xg=grid[0]
    Nx=len(input[0])
    x=X[0]
    dt=delta[0]
    dx=delta[1]
    if(x==0):
        return 0
    elif(x==Nx-1):
        return 0
    else:
        alpha=0.0025
        o=u[x]
        o_xm1=u[x-1]
        o_xp1=u[x+1]
        A=o*(o_xp1-o_xm1)/(2*dx)
        B=(o_xp1-2*o+o_xm1)/(dx**2)
        result=o+dt*(A+alpha*B)
        return result
def init1(N):
    xg=np.linspace(0,1,N)
    B=np.zeros([N],dtype=float)
    for x in range(0,N):
                B[x]=np.sin(xg[x])
    return B

N=100
x=np.linspace(0,1,N)
y=np.linspace(0,1,N)
#this is the proper way to read in values from meshgrid consider the first matrix to be y
#and the second matrix to be x it is a far more intuitive way to deal with the matrices
yy,xx=np.meshgrid(x,y)

grid=[x]

matrix1=init1(N)
#matrix2=np.zeros([N,N],dtype=float)
Lm=[matrix1]
f=[function1]
#funcx=[func1x,func2x]
#funcy=[func1y,func2y]
#fI=[diag1,diag1]
#X,t=multipdesys2dIET(Lm,grid,funcx,funcy,fI,fI,0,1,0.01)
X,t=multipdesys1D(Lm,grid,f,0,1,0.0001)

array=list(X.values())
m0=array[0][0]
m1=array[0][int(0.005/0.0001)]
m2=array[0][int(0.01/0.0001)]
m3=array[0][int(0.025/0.0001)]
m4=array[0][int(0.25/0.0001)]
figure1=plt.figure()
ax=figure1.add_subplot()
ax.plot(x,m0,label="t=0")
ax.plot(x,m1,label="t=0.005")
ax.plot(x,m2,label="t=0.01")
ax.plot(x,m3,label="t=0.025")
ax.plot(x,m4,label="t=0.25")
ax.set_xlabel("x")
ax.set_ylabel("u")
ax.legend()
figure1.suptitle(" Burger equation")
plt.show()
