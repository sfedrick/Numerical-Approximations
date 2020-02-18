# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 07:26:17 2020

@author: shaun
"""
import numpy as np
import matplotlib.pyplot as plt
def function(x):
    f=np.sin(5*x)
    return f
def actual(x):
    f=5*np.cos(5*x)
    return f
def given(h,x):
    y1=function(x-h)
    y2=function(x)
    y3=function(x+h)
    y=(y1-2*y2+y3)/(h**2)
    return y
def derived(h,x):
    y1=function(x-2*h)
    y2=function(x)
    y3=function(x+2*h)
    y=(y1-2*y2+y3)/(4*(h**2))
    return y
h=np.linspace(10**(-4),1,1000)
poperror=((given(h,1.5)-actual(1.5))**2)**0.5
deriverror=((derived(h,1.5)-actual(1.5))**2)**0.5
figure=plt.figure()
ax=figure.add_subplot(111)
figure.suptitle("Error of Second derivative")
ax.plot(h,poperror,marker="o",label="Popular Second derivative Formula")
ax.plot(h,deriverror,marker="x", label="Derived second derivative Formula")
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend()
