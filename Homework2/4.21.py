from odesolversystem import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

k1=0.04
k2=10.0
k3=1.5*10**3
def dC1(X,t):
    c1=X[0]
    c2=X[1]
    c3=X[2]
    dc1=-k1*c1+k2*c2*c3
    return dc1
def dC2(X,t):
    c1=X[0]
    c2=X[1]
    c3=X[2]
    dc2=k1*c1-k2*c2*c3-2*k3*(c2**2)
    return dc2
def dC3(X,t):
    c1=X[0]
    c2=X[1]
    c3=X[2]
    dc3=2*k3*(c2**2)
    return dc3
def df(X):
    c1=X[0]
    c2=X[1]
    c3=X[2]
    row1=[-k1,k2*c3,k2*c2]
    row2=[k1,-k2*c3-4*k3*c2,-k2*c2]
    row3=[0,4*k3*c2,0]
    J=np.array([row1,row2,row3])
    return J
def DF(y,t):
    c1,c2,c3=y
    dydt=[-k1*c1+k2*c2*c3, k1*c1-k2*c2*c3-2*k3*(c2**2), 2*k3*(c2**2)]
    return dydt
funclist=[dC1,dC2,dC3]

Bigc,rt=odesysRk4([0.9,0.1,0],0,3000,0.002,funclist,3)
c1,c2,c3=Bigc.values()
Bigtt,tt=eulerIlin([0.9,0.1,0],0,3000,0.1,funclist,df,3)
tc1,tc2,tc3=Bigtt.values()
t=np.linspace(0,3000,30000)
sol=odeint(DF,[0.9,0.1,0],t)

figure=plt.figure()
ax=figure.add_subplot()
ax.loglog(rt,c1,label="Concentration 1")
ax.loglog(rt,c2,label="Concentration 2")
ax.loglog(rt,c3,label="Concentration 3")
ax.legend()
ax.set_xlabel("Time")
ax.set_ylabel("Concentration  Percentage")
figure.suptitle("concentrations versus time rungekuta4")

figure1=plt.figure()
ax1=figure1.add_subplot()
ax1.loglog(tt,tc1,label="Concentration 1")
ax1.loglog(tt,tc2,label="Concentration 2")
ax1.loglog(tt,tc3,label="Concentration 3")
ax1.legend()
ax1.set_xlabel("Time")
ax1.set_ylabel("Concentration  Percentage")
figure1.suptitle("concentrations versus time linearized trapezoidal")


figure2=plt.figure()
ax2=figure2.add_subplot()
ax2.loglog(t,sol[:,0],label="Concentration 1")
ax2.loglog(t,sol[:,1],label="Concentration 2")
ax2.loglog(t,sol[:,2],label="Concentration 3")
ax2.legend()
ax2.set_xlabel("Time")
ax2.set_ylabel("Concentration  Percentage")
figure2.suptitle("concentrations versus time Stiff solver")
plt.show()
