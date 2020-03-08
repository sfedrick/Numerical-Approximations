import numpy as np
import matplotlib.pyplot as plt
from odesolversystem import *

def EE(X,Y):
    Z=((x)**2+(y)**2)**(0.5)
    return Z
x=np.linspace(-10,10,1000)
y=np.linspace(-10,10,1000)
X,Y=np.meshgrid(x,y)
Z=EE(X,Y)
figure=plt.figure()
ax=figure.add_subplot()
ax.contour(X,Y,Z)
plt.show()
