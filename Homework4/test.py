import numpy as np
import pandas as pd
from multipdesys import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import random
def diag1(row,grid,delta):
    a=[]
    b=[]
    c=[]
    alpha=1
    for i in range(0,row):
        if(i==0):
            b.append(1)
            c.append(0)
        elif(i==row-1):
            a.append(0)
            b.append(1)
        else:
            a.append(-(2.0*alpha*delta[0])/(delta[1]**2))
            b.append((2.0*alpha*delta[0])/(delta[1]**2)+1)
            c.append(-(2.0*alpha*delta[0])/(delta[1]**2))
    return [a,b,c]
def function1(X,grid,input,delta):
    u=input[0]
    #v=input[1]
    Nx,Ny=input[0].shape
    xg=grid[0]
    yg=grid[1]
    x=X[0]
    y=X[1]
    dt=delta[0]
    dx=delta[1]
    dy=delta[2]
    if(x==0):
        return 0
    elif(x==Nx-1):
        return 0
    elif(y==0):
        return 0
    elif(y==Ny-1):
        return 0
    else:
        alpha=1
        o=u[x,y]
        q=0
        o_xm1=u[x-1,y]
        o_xp1=u[x+1,y]
        o_ym1=u[x,y-1]
        o_yp1=u[x,y+1]
        A=-o*((o_xp1-o_xm1)/(2*dx))
        B=-q*((o_yp1-o_ym1)/(2*dy))
        C=(o_xp1-2*o+o_xm1)/(dx**2)
        D=(o_yp1-2*o+o_ym1)/(dy**2)
        #result=o+dt*(A+B+alpha*(C+D))
        #result=o+dt*(C+D)
        result=o+dt*(alpha*(C+D)+2*(2-xg[x,y]**2-yg[x,y]**2))
        return result

def func(X,grid,input,delta):
    u=input[0]
    #v=input[1]
    Nx,Ny=input[0].shape
    xg=grid[0]
    yg=grid[1]
    x=X[0]
    y=X[1]
    dt=delta[0]
    dx=delta[1]
    dy=delta[2]
    if(x==0):
        return 0
    elif(x==Nx-1):
        return 0
    elif(y==0):
        return 0
    elif(y==Ny-1):
        return 0
    else:
        alpha=1
        o=u[x,y]
        q=0
        o_xm1=u[x-1,y]
        o_xp1=u[x+1,y]
        o_ym1=u[x,y-1]
        o_yp1=u[x,y+1]
        A=-o*((o_xp1-o_xm1)/(2*dx))
        B=-q*((o_yp1-o_ym1)/(2*dy))
        C=(o_xp1-2*o+o_xm1)/(dx**2)
        D=(o_yp1-2*o+o_ym1)/(dy**2)
        #result=o+dt*(A+B+alpha*(C+D))
        #result=o+dt*(C+D)
        result=o+dt*(alpha*(D)+2*(2-xg[x,y]**2-yg[x,y]**2))
        return result
def gunc(X,grid,input,delta):
    u=input[0]
    #v=input[1]
    Nx,Ny=input[0].shape
    xg=grid[0]
    yg=grid[1]
    x=X[0]
    y=X[1]
    dt=delta[0]
    dx=delta[1]
    dy=delta[2]
    if(x==0):
        return 0
    elif(x==Nx-1):
        return 0
    elif(y==0):
        return 0
    elif(y==Ny-1):
        return 0
    else:
        alpha=1
        o=u[x,y]
        q=0
        o_xm1=u[x-1,y]
        o_xp1=u[x+1,y]
        o_ym1=u[x,y-1]
        o_yp1=u[x,y+1]
        A=-o*((o_xp1-o_xm1)/(2*dx))
        B=-q*((o_yp1-o_ym1)/(2*dy))
        C=(o_xp1-2*o+o_xm1)/(dx**2)
        D=(o_yp1-2*o+o_ym1)/(dy**2)
        #result=o+dt*(A+B+alpha*(C+D))
        #result=o+dt*(C+D)
        result=o+dt*(alpha*(C)+2*(2-xg[x,y]**2-yg[x,y]**2))
        return result
def init1(N):
    A=np.zeros([N,N],dtype=float)
    for x in range(0,N):
        for y in range(0,N):
            if(x==0):
                A[x,y]=0
            elif(x==N-1):
                A[x,y]=0
            elif(y==0):
                A[x,y]=np.sin(2*np.pi*x)
            elif(y==N-1):
                A[x,y]=np.sin(2*np.pi*x)
            else:
                A[x,y]=np.sin(2*np.pi*x)
    return A
def init2(N):
    A=np.zeros([N,N],dtype=float)
    for x in range(0,N):
        for y in range(0,N):
            if(x==0):
                A[x,y]=1.0-y
            elif(x==N-1):
                A[x,y]=1.0-y
            elif(y==0):
                A[x,y]=0
            elif(y==N-1):
                A[x,y]=0
            else:
                A[x,y]=1.0-y
    return A

N=20
x=np.linspace(-1,1,N)
y=np.linspace(-1,1,N)
yy,xx=np.meshgrid(x,y)
grid=[xx,yy]
#matrix1=init1(N)
matrix2=init2(N)
matrix1=np.zeros([N,N],dtype=float)
#matrix2=np.zeros([N,N],dtype=float)
Lm=[matrix1]
f=[func]
g=[gunc]

fI=[diag1]
X,t=multipdesys2dIET(Lm,grid,f,g,fI,fI,0,1,0.001)
#X,t=multipdesys2dEE(Lm,grid,f,0,1,0.001)
array=list(X.values())
m1=array[0][-1]
m10=array[0][0]
#m2=array[1][-1]
#m20=array[1][0]

figure1=plt.figure()
ax=mplot3d.Axes3D(figure1)
ax.plot_surface(xx,yy,m1,cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Velocity")
figure1.suptitle("U Velocity")



figure3=plt.figure()
ax=mplot3d.Axes3D(figure3)
ax.plot_surface(xx,yy,m10,cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Velocity")
figure3.suptitle("init U Velocity")
plt.show()
