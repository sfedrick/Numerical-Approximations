import numpy as np
import matplotlib.pyplot as plt
from odesolvers412 import *

def anal(y0,t):
    yt=-np.log(np.e**(-y0)+np.e**(-t)-1)
    return yt
def solveode(y,t):
    dydt=np.e**(y-t)
    return dydt
def dfdt(y,t):
    dydt=-np.e**(y-t)
    return dydt
o=-1*10**(-5)
tact=np.linspace(0,100,501)
act=anal(o,tact)
tlini,ylini=eulerIlin(o,0,100,0.2,solveode,dfdt)
#ti,yi=eulerI(o,0,100,0.2,solveode)
error= abs(act-ylini)/abs(act)
figure=plt.figure()
ax=figure.add_subplot()
ax.plot(tlini,ylini,label="linearized implicit")
ax.plot(tact,act,label="actual solution")
#ax.plot(ti,yi,label="Fully implicit")
ax.plot(tact,error,label="Error")
ax.set_xlabel("Y(t)")
ax.set_ylabel("$Time$")
ax.set_title("y0=-1*10^-5")
ax.legend()


o=-1
tact2=np.linspace(0,100,501)
act2=anal(o,tact2)

tlini2,ylini2=eulerIlin(o,0,100,0.2,solveode,dfdt)
error2= abs(act2-ylini2)/abs(act2)
figure2=plt.figure()
ax1=figure2.add_subplot()
ax1.plot(tlini2,ylini2,label="linearized implicit")
ax1.plot(tact2,act2,label="actual solution")
ax1.plot(tact2,error2,label="Error")
ax1.set_xlabel("Y(t)")
ax1.set_ylabel("$Time$")
ax1.set_title("y0=-1")
ax1.legend()
plt.show()
