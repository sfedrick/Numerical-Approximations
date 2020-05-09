import numpy as np
import matplotlib.pyplot as plt
from pandas.core.common import flatten
from fourierMethods import *
from multipdesys import *
from mpl_toolkits import mplot3d
N=64
def g(x,y):
    z=-100*np.sin(6*x)*np.cos(8*y)
    return z
x=np.linspace(0,2*np.pi,N)
y=np.linspace(0,2*np.pi,N)
yy,xx=np.meshgrid(x,y)
q=g(xx,yy)

K=findK(N)

Fq=np.fft.fft2(q)/N

F=np.zeros([N,N])
for i in range(0,q.shape[0]):
    for j in range(0,q.shape[1]):
        if(K[i]==0 or K[j]==0):
            F[i][j]=0
        else:
            F[i][j]=(-Fq[i][j])/(K[i]**2+K[j]**2)
F[0][0]=F[0][0];
ans=np.fft.ifft2(F*N)
ans=abs(ans)

figure1=plt.figure()
ax=figure1.add_subplot(projection='3d')
ax.plot_surface(xx,yy,ans)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
figure1.suptitle("3d plot")
plt.show()
