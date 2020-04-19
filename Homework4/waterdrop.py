import numpy as np
import pandas as pd
from multipdesys import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def safediv(n,d):
    if(d==0 or d<0.001):
        return 0
    else:
        return (n/d)
def function1(X,grid,input,delta):
    p=np.copy(input[0])
    pu=np.copy(input[1])
    pv=np.copy(input[2])
    Nx,Ny=input[0].shape
    x=X[0]
    y=X[1]
    xg=grid[0]
    yg=grid[1]
    dt=delta[0]
    dx=delta[1]
    dy=delta[2]
    if(y==0):
        return pu[x,y]
    elif(y==Nx-1):
        return 0
    elif(x==0):
        return pv[x,y]
    elif(x==Ny-1):
        return pv[x,y]
    else:
        fx=0.5*(dt/dx)
        F1=0.5*(p[x+1,y]+p[x-1,y])
        F2=(p[x+1,y]*(safediv(pu[x+1,y],p[x+1,y])))
        F3=(p[x-1,y]*(safediv(pu[x-1,y],p[x-1,y])))
        gy=-0.5*(dt/dy)
        G1=0.5*(p[x,y+1]+p[x,y+1])
        G2=(p[x,y+1]*(safediv(pv[x,y+1],p[x,y+1])))
        G3=(p[x,y-1]*(safediv(pv[x,y-1],p[x,y-1])))
        np1=F1-fx*(F2-F3)+G1-gy*(G2-G3)
        return np1
def function2(X,grid,input,delta):
    p=np.copy(input[0])
    pu=np.copy(input[1])
    pv=np.copy(input[2])
    Nx,Ny=input[0].shape
    x=X[0]
    y=X[1]
    xg=grid[0]
    yg=grid[1]
    dt=delta[0]
    dx=delta[1]
    dy=delta[2]
    if(y==0):
        return (p[x,y]*(safediv(pu[x,y],p[x,y]))**2)+2*9.8*p[x,y]**2
    elif(y==Nx-1):
        return (p[x,y]*(safediv(pu[x,y],p[x,y]))**2)+2*9.8*p[x,y]**2
    elif(x==0):
        return 9.8*p[x,y]**2
    elif(x==Ny-1):
        return 9.8*p[x,y]**2
    else:
        fx=0.5*(dt/dx)
        F1=0.5*(pu[x+1,y]+pu[x-1,y])
        F2=(p[x+1,y]*((safediv(pu[x+1,y],p[x+1,y]))**2))+0.5*9.8*(p[x+1,y]**2)
        F3=(p[x-1,y]*((safediv(pu[x-1,y],p[x-1,y]))**2))+0.5*9.8*(p[x-1,y]**2)
        gy=0.5*(dt/dy)
        G1=0.5*(pu[x,y+1]+pu[x,y+1])
        G2=(pu[x,y+1]*(safediv(pv[x,y-1],p[x,y-1])))
        G3=(pu[x,y-1]*(safediv(pv[x,y+1],p[x,y+1])))
        np1=F1-fx*(F2-F3)+G1-gy*(G2-G3)
        return np1
def function3(X,grid,input,delta):
        p=np.copy(input[0])
        pu=np.copy(input[1])
        pv=np.copy(input[2])
        Nx,Ny=input[0].shape
        x=X[0]
        y=X[1]
        xg=grid[0]
        yg=grid[1]
        dt=delta[0]
        dx=delta[1]
        dy=delta[2]
        if(y==0):
            return 0.5*9.8*p[x,y]**2
        elif(y==Nx-1):
            return 0.5*9.8*p[x,y]**2
        elif(x==0):
            return (p[x,y]*(safediv(pu[x,y],p[x,y]))**2)+2*9.8*p[x,y]**2
        elif(x==Ny-1):
            return (p[x,y]*(safediv(pu[x,y],p[x,y]))**2)+2*9.8*p[x,y]**2
        else:
            fx=0.5*(dt/dx)
            F1=0.5*(pu[x+1,y]+pu[x-1,y])
            F2=(pv[x+1,y]*(safediv(pv[x+1,y],p[x+1,y])))
            F3=(pv[x-1,y]*(safediv(pv[x-1,y],p[x-1,y])))
            gy=0.5*(dt/dy)
            G1=0.5*(pu[x,y+1]+pu[x,y+1])
            G2=((p[x,y+1]*(safediv(pv[x,y+1],p[x,y+1]))**2))+0.5*9.8*(p[x,y+1]**2)
            G3=((p[x,y-1]*(safediv(pv[x,y-1],p[x,y-1]))**2))+0.5*9.8*(p[x,y+1]**2)
            np1=F1-fx*(F2-F3)+G1-gy*(G2-G3)
            return np1

def init1(N,grid):
    xg=grid[0]
    yg=grid[1]
    x0=0
    y0=0
    h=-0.02
    w=5*10**(-4)
    B=np.zeros([N,N],dtype=float)
    for x in range(0,N):
        for y in range(0,N):
                B[x,y]=1+h*np.e**(-((( xg[x,y]-x0)**2)+((yg[x,y]-y0)**2))/w)
    return B
N=40
x=np.linspace(0,1,N)
y=np.linspace(0,1,N)
#this is the proper way to read in values from meshgrid consider the first matrix to be y
#and the second matrix to be x it is a far more intuitive way to deal with the matrices
yy,xx=np.meshgrid(x,y)

grid=[xx,yy]
matrix1=init1(N,grid)
matrix2=np.zeros([N,N],dtype=float)
matrix3=np.zeros([N,N],dtype=float)
Lm=[matrix1,matrix2,matrix3]
f=[function1,function2,function3]

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
figure1.suptitle("P")



plt.show()
