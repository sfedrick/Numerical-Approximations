import numpy as np
import pandas as pd
from multipdesys import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import random
from odesolversystem import *
def function1(X,grid,input,delta):
    u=X
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
        return 0
    elif(y==Ny-1):
        return 0
    else:
        alpha=0.0025
        o=u[x,y]
        o_xm1=u[x-1]
        o_xp1=u[x+1]
        A=o*(o_xp1-o_xm1)/(2*dx)
        B=(o_xp1-2*o+o_xm1)/(dx**2)
        result=(A+alpha*B)
        return result
def initvector(a,b,N):
    xinit=[]
    X=np.linspace(a,b,N)
    for x in X:
        if(0<=x and x<=0.2):
            xinit.append(1.0-(10.0*x-1.0)**2)
        else:
            xinit.append(0)
    return xinit
