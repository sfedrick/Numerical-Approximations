from odesolversystem import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
r=20
def f1(X,t):
    x=X[0]
    y=X[1]
    sig=10
    dx=sig*(y-x)
    return dx
def f2(X,t):
    x=X[0]
    y=X[1]
    z=X[2]
    dy=r*x-y-x*z
    return dy
def f3(X,t):
    x=X[0]
    y=X[1]
    z=X[2]
    b=8.0/3
    dz=x*y-b*z
    return dz
funclist=[f1,f2,f3]

Bigx,t=odesysRk4([1,1,1],0,25,0.002,funclist,3)
x,y,z=Bigx.values()
figure=plt.figure()
ax=figure.add_subplot()
ax.plot(x,z)
ax.set_xlabel("x")
ax.set_ylabel("z")
figure.suptitle("r=20")
figure1=plt.figure()
ax1=figure1.add_subplot()
ax1.plot(x,y)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
figure1.suptitle("r=20")
figure2=plt.figure()
ax2=figure2.add_subplot()
ax2.plot(y,z)
ax2.set_xlabel("y")
ax2.set_ylabel("z")
figure2.suptitle("r=20")
figure3=plt.figure()
ax3=figure3.gca(projection='3d')
figure3.suptitle("r=20")
ax3.plot(x,y,z,label="Parametric curve")

r=28
BigX,t=odesysRk4([1,1,1],0,25,0.002,funclist,3)
x1,y1,z1=BigX.values()
figure4=plt.figure()
ax4=figure4.gca(projection='3d')
figure4.suptitle("r=28")
ax4.plot(x1,y1,z1,label="Parametric curve")
plt.show()

r=28
BigX2,t=odesysRk4([6,6,6],0,25,0.002,funclist,3)
x2,y2,z2=BigX2.values()
BigX3,t=odesysRk4([6,6.01,6],0,25,0.002,funclist,3)
x3,y3,z3=BigX3.values()
figure5=plt.figure()
ax5=figure5.gca(projection='3d')
figure5.suptitle("r=28")
ax5.plot(x2,y2,z2,label="Intial= (6, 6, 6)")
ax5.plot(x3,y3,z3,label="Intial= (6, 6.01, 6)")
ax5.legend()
plt.show()
