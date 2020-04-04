import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def func(kdx):
    l=2-np.cos(3*kdx)+4*np.cos(2*kdx)-5*np.cos(kdx)
    return l
kdx=np.linspace(0,4,1000)
lr=func(kdx)
figure=plt.figure()
ax=figure.add_subplot()
ax.plot(kdx,lr)
ax.set_ylabel(r'$\lambda_{r} \frac{\Delta x^{2}}{\alpha}$')
ax.set_xlabel(r'$k \Delta x$')
plt.show()
