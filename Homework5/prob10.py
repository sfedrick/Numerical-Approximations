import numpy as np
from gaussxw import *
from integration import *

def f(x):
    y=np.log(x)/x
    return y
def G1d(a,b,x,w,N,f):
    #global N
    #global x
    #global w
    #rescale x and weights to the domain
    xp=0.5*(b-a)*x + 0.5*(b+a)
    wpx=0.5*(b-a)*w
    s=0
    for xm in range(0,N):
        #find the value of the function at every y and multiply it by the weights to get the sum
            s+=wpx[xm]*f(xp[xm])
    return s
N=[2,4,8,12,16]
G=[]
S=[]
exact=2.1620386
for n in N:
    x,w=gaussxw(n)
    t1,t2,s=swhole(n,1,8,f)
    G.append(G1d(1,8,x,w,n,f))
    S.append(s)
G=np.array(G)
S=np.array(S)
ErrorG=abs(G-exact)
ErrorS=abs(S-exact)

figure1=plt.figure()
ax=figure1.add_subplot()
ax.loglog(N,ErrorG,label="Error Gaussian",color='green')
ax.loglog(N,ErrorS,label="Error Midpoint",color='blue')
ax.set_xlabel("x")
ax.set_ylabel("absolute error")
ax.legend(loc='best')
figure1.suptitle("Error of each method")
plt.show()
