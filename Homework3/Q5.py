from odesolversystem import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def constant(N):
    A=np.zeros((N,N))
    dx=1/N
    for diag in range(1,N):
        if (diag==0):
            A[diag][diag]=1/dx
            A[diag][diag+1]=-2/dx
        elif(diag>0 and diag<N-1):
            A[diag][diag-1]=1/dx
            A[diag][diag]=-2/dx
            A[diag][diag+1]=1/dx
        elif(diag==N-1):
            A[diag][diag-1]=1/dx
            A[diag][diag]=-2/dx
    return A


def mixedboundary(N):
    A=np.zeros((N,N))
    dx=1/N
    a=3/(dx**2)
    b=(2*al)/dx
    A1=(-1/(a+b))+(1/(dx**2))
    B2=(4/(a+b))+(-2/(dx**2))
    for diag in range(1,N):
        if (diag==0):
            A[diag][diag]=-2/dx
            A[diag][diag+1]=1/dx
        elif(diag>0 and diag<N-1):
            A[diag][diag-1]=1/dx
            A[diag][diag]=-2/dx
            A[diag][diag+1]=1/dx
        elif(diag==N-1):
            A[diag][diag-1]=A1
            A[diag][diag]=B2
    return A

def ghostpoint(N):
    A=np.zeros((N,N))
    dx=1/N
    A1=2/(dx**2)
    B2=(-2*dx*al+2)/(dx**2)
    for diag in range(1,N):
        if (diag==0):
            A[diag][diag]=-2/dx
            A[diag][diag+1]=1/dx
        elif(diag>0 and diag<N-1):
            A[diag][diag-1]=1/dx
            A[diag][diag]=-2/dx
            A[diag][diag+1]=1/dx
        elif(diag==N-1):
            A[diag][diag-1]=A1
            A[diag][diag]=B2
    return A


varyN=np.linspace(10,10**3,4)
MNeigen=[]
for n in varyN:
    al=1
    n=int(n)
    A=mixedboundary(n)
    eigen= abs(np.linalg.eigvals(A))
    eigen=np.sort(eigen)
    MNeigen.append(eigen[-1])
varyal=np.linspace(0,10,10)
MAleigen=[]
for n in varyal:
    al=n
    A=mixedboundary(100)
    eigen=abs(np.linalg.eigvals(A))

    eigen=np.sort(eigen)
    MAleigen.append(eigen[-1])

GNeigen=[]
for n in varyN:
    al=1
    n=int(n)
    A=ghostpoint(n)
    eigen= abs(np.linalg.eigvals(A))
    eigen=np.sort(eigen)
    GNeigen.append(eigen[-1])

GAleigen=[]
for n in varyal:
    al=n
    A=ghostpoint(100)
    eigen=abs(np.linalg.eigvals(A))
    eigen=np.sort(eigen)
    GAleigen.append(eigen[-1])


CNeigen=[]
for n in varyN:
    al=1
    n=int(n)
    A=constant(n)
    eigen= abs(np.linalg.eigvals(A))
    eigen=np.sort(eigen)
    CNeigen.append(eigen[-1])
varyal=np.linspace(0,10,10)
CAleigen=[]
for n in varyal:
    al=n
    A=constant(100)
    eigen=abs(np.linalg.eigvals(A))
    eigen=np.sort(eigen)
    CAleigen.append(eigen[-1])

figure=plt.figure()
ax=figure.add_subplot()
ax.loglog(varyN,MNeigen,label="Mixed Boundary")
ax.loglog(varyN,CNeigen,label="Dirichelet")
ax.legend()
figure.suptitle("Vary N mixed boundary")


figure2=plt.figure()
ax=figure2.add_subplot()
ax.plot(varyal,MAleigen,label="Mixed Boundary")
ax.plot(varyal,CAleigen,label="Dirichelet")
ax.legend()
figure2.suptitle("vary alpha mixed boundary")



figure=plt.figure()
ax=figure.add_subplot()
ax.loglog(varyN,GNeigen,label="Ghost points")
ax.loglog(varyN,CNeigen,label="Dirichelet")
ax.legend()
figure.suptitle("Vary N ghost points")


figure2=plt.figure()
ax=figure2.add_subplot()
ax.plot(varyal,GAleigen,label="Ghost Points")
ax.plot(varyal,CAleigen,label="Dirichelet")
ax.legend()
figure2.suptitle("vary alpha ghost points")

plt.show()
