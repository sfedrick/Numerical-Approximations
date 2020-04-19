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
    alpha=0.015
    for i in range(0,row):
        if(i==0):
            b.append(1)
            c.append(0)
        elif(i==row-1):
            a.append(0)
            b.append(1)
        else:
            a.append(-(2*alpha*delta[0])/(delta[1]**2))
            b.append((2*alpha*delta[0])/(delta[1]**2)+2)
            c.append(-(2*alpha*delta[0])/(delta[1]**2))
    return [a,b,c]
def func1x(X,grid,input,delta):
    u=input[0]
    v=input[1]
    xg=grid[0]
    yg=grid[1]
    Nx,Ny=input[0].shape
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
        return np.sin(2*np.pi*xg[x,y])
    elif(y==Ny-1):
        return np.sin(2*np.pi*xg[x,y])
    else:
        alpha=0.015
        o=u[x,y]
        q=v[x,y]
        o_xm1=u[x-1,y]
        o_xp1=u[x+1,y]
        o_ym1=u[x,y-1]
        o_yp1=u[x,y+1]
        A=-o*((o_xp1-o_xm1)/(2*dx))
        B=-q*((o_yp1-o_ym1)/(2*dy))
        C=(o_xp1-2*o+o_xm1)/(dx**2)
        D=(o_yp1-2*o+o_ym1)/(dy**2)
        #result=2*o+dt*(A+B+(alpha*(D)))
        result=o+dt*((alpha*(C)))
        return result
def func1y(X,grid,input,delta):
    u=input[0]
    v=input[1]
    xg=grid[0]
    yg=grid[1]
    Nx,Ny=input[0].shape
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
        return np.sin(2*np.pi*xg[x,y])
    elif(y==Ny-1):
        return np.sin(2*np.pi*xg[x,y])
    else:
        alpha=0.015
        o=u[x,y]
        q=v[x,y]
        o_xm1=u[x-1,y]
        o_xp1=u[x+1,y]
        o_ym1=u[x,y-1]
        o_yp1=u[x,y+1]
        A=-o*((o_xp1-o_xm1)/(2*dx))
        B=-q*((o_yp1-o_ym1)/(2*dy))
        C=(o_xp1-2*o+o_xm1)/(dx**2)
        D=(o_yp1-2*o+o_ym1)/(dy**2)
        #result=2*o+dt*(A+B+(alpha*(C)))
        result=o+dt*((alpha*(C)))
        return result
def func2x(X,grid,input,delta):
    u=input[0]
    v=input[1]
    xg=grid[0]
    yg=grid[1]
    Nx,Ny=input[0].shape
    x=X[0]
    y=X[1]
    dt=delta[0]
    dx=delta[1]
    dy=delta[2]
    if(x==0):
        return 1.0-yg[x,y]
    elif(x==Nx-1):
        return 1.0-yg[x,y]
    elif(y==0):
        return 1.0
    elif(y==Ny-1):
        return 0
    else:
        alpha=0.015
        o=v[x,y]
        q=u[x,y]
        o_xm1=v[x-1,y]
        o_xp1=v[x+1,y]
        o_ym1=v[x,y-1]
        o_yp1=v[x,y+1]
        A=-q*((o_xp1-o_xm1)/(2*dx))
        B=-o*((o_yp1-o_ym1)/(2*dy))
        C=(o_xp1-2*o+o_xm1)/(dx**2)
        D=(o_yp1-2*o+o_ym1)/(dy**2)
        #result=2*o+dt*(A+B+(alpha*(D)))
        result=o+dt*((alpha*(C)))
        return result
def func2y(X,grid,input,delta):
    u=input[0]
    v=input[1]
    xg=grid[0]
    yg=grid[1]
    Nx,Ny=input[0].shape
    x=X[0]
    y=X[1]
    dt=delta[0]
    dx=delta[1]
    dy=delta[2]
    if(x==0):
        return 1.0-yg[x,y]
    elif(x==Nx-1):
        return 1.0-yg[x,y]
    elif(y==0):
        return 1.0
    elif(y==Ny-1):
        return 0
    else:
            alpha=0.015
            o=v[x,y]
            q=u[x,y]
            o_xm1=v[x-1,y]
            o_xp1=v[x+1,y]
            o_ym1=v[x,y-1]
            o_yp1=v[x,y+1]
            A=-q*((o_xp1-o_xm1)/(2*dx))
            B=-o*((o_yp1-o_ym1)/(2*dy))
            C=(o_xp1-2*o+o_xm1)/(dx**2)
            D=(o_yp1-2*o+o_ym1)/(dy**2)
            #result=o+dt*(A+B+(alpha*(C)))
            result=o+dt*((alpha*(C)))
            return result
def function1(X,grid,input,delta):
    u=input[0]
    v=input[1]
    xg=grid[0]
    yg=grid[1]
    Nx,Ny=input[0].shape
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
        return np.sin(2*np.pi*xg[x,y])
    elif(y==Ny-1):
        return np.sin(2*np.pi*xg[x,y])
    else:
        alpha=0.015
        o=u[x,y]
        q=v[x,y]
        o_xm1=u[x-1,y]
        o_xp1=u[x+1,y]
        o_ym1=u[x,y-1]
        o_yp1=u[x,y+1]
        A=-o*((o_xp1-o_xm1)/(2*dx))
        B=-q*((o_yp1-o_ym1)/(2*dy))
        C=(o_xp1-2*o+o_xm1)/(dx**2)
        D=(o_yp1-2*o+o_ym1)/(dy**2)
        result=o+dt*(A+B+(alpha*(C+D)))
        return result

def function2(X,grid,input,delta):
    u=np.copy(input[0])
    v=np.copy(input[1])
    Nx,Ny=input[0].shape
    x=X[0]
    y=X[1]
    xg=grid[0]
    yg=grid[1]
    dt=delta[0]
    dx=delta[1]
    dy=delta[2]
    if(x==0):
        return 1.0-yg[x,y]
    elif(x==Nx-1):
        return 1.0-yg[x,y]
    elif(y==0):
        return 1.0
    elif(y==Ny-1):
        return 0
    else:
        alpha=0.015
        o=v[x,y]
        q=u[x,y]
        o_xm1=v[x-1,y]
        o_xp1=v[x+1,y]
        o_ym1=v[x,y-1]
        o_yp1=v[x,y+1]
        A=-q*((o_xp1-o_xm1)/(2*dx))
        B=-o*((o_yp1-o_ym1)/(2*dy))
        C=(o_xp1-2*o+o_xm1)/(dx**2)
        D=(o_yp1-2*o+o_ym1)/(dy**2)
        result=o+dt*(A+B+(alpha*(C+D)))
        return result

def init1(N):
    xg=grid[0]
    yg=grid[1]
    B=np.zeros([N,N],dtype=float)
    for x in range(0,N):
        for y in range(0,N):
            if(x==0):
                B[x,y]=0
            elif(x==N-1):
                B[x,y]=0
            elif(y==0):
                B[x,y]=np.sin(2*np.pi*xg[x,y])
            elif(y==N-1):
                B[x,y]=np.sin(2*np.pi*xg[x,y])
            else:
                B[x,y]=0
    return B
def init2(N):
    xg=grid[0]
    yg=grid[1]
    A=np.zeros([N,N],dtype=float)
    for x in range(0,N):
        for y in range(0,N):
            if(x==0):
                A[x,y]=1.0-yg[x,y]
            elif(x==N-1):
                A[x,y]=1.0-yg[x,y]
            elif(y==0):
                A[x,y]=0
            elif(y==N-1):
                A[x,y]=0
            else:
                A[x,y]=0
    return A

N=40
x=np.linspace(0,1,N)
y=np.linspace(0,1,N)
#this is the proper way to read in values from meshgrid consider the first matrix to be y
#and the second matrix to be x it is a far more intuitive way to deal with the matrices
yy,xx=np.meshgrid(x,y)

grid=[xx,yy]
matrix1=init1(N)
matrix2=init2(N)
#matrix1=np.zeros([N,N],dtype=float)
#matrix2=np.zeros([N,N],dtype=float)
Lm=[matrix1,matrix2]
f=[function1,function2]
funcx=[func1x,func2x]
funcy=[func1y,func2y]
fI=[diag1,diag1]
#X,t=multipdesys2dIET(Lm,grid,funcx,funcy,fI,fI,0,1,0.01)
X,t=multipdesys2dEE(Lm,grid,f,0,5,0.01)

array=list(X.values())
m1=array[0][-1]
m10=array[0][0]
m2=array[1][-1]
m20=array[1][0]



figure1=plt.figure()
ax=mplot3d.Axes3D(figure1)
ax.plot_surface(xx,yy,m1,cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Velocity")
figure1.suptitle("U Velocity")


figure2=plt.figure()
ax=mplot3d.Axes3D(figure2)
ax.plot_surface(xx,yy,m2,cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Velocity")
figure2.suptitle("V Velocity")


figure3=plt.figure()
ax=mplot3d.Axes3D(figure3)
ax.plot_surface(xx,yy,m10,cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Velocity")
figure3.suptitle("init U Velocity")


figure4=plt.figure()
ax=mplot3d.Axes3D(figure4)
ax.plot_surface(xx,yy,m20,cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Velocity")
figure4.suptitle("init V Velocity")
plt.show()
