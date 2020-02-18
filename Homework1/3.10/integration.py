# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:25:30 2020

@author: shaun
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def function(x):
    function=(100/((x+0.1)**(0.5)))+(1.0/(((x-0.3)**2)+0.001))-np.pi   
    return function
def fderiv(x):
    a=50/((x+1/100.0)**(3.0/2))
    b=2*(x-0.3)
    c=((x-0.3)**2)+(1/1000)
    c=c**2
    f=-a-(b/c)
    return f


def rpart(y,delta):
    sumx=y*delta
    return sumx

def tpart(y1,y2,delta):
    sumx=((y1+y2)/2.0)*delta
    return sumx

def spart(y1,y2,y3,delta):
    sumx=(float(delta)/3.0)*(y1+(4.0*y2)+y3) 
    return sumx

def rwhole(N,a,b,left):
    listx=np.linspace(a,b,N)
    listy=[]
    sumx=0
    if(left==True):
        for x in range(0,N):
            if(x<N-1):
                y1=function(listx[x])
                delta=listx[x]-listx[x+1]
                delta=(delta**2)**(0.5)
                sumx+= rpart(y1,delta)
                listy.append(sumx)
            else :
                return sumx
    else:
         for x in range(0,N):
            if(x<N-2):
                y2=function(listx[x+1])
                delta=listx[x]-listx[x+1]
                delta=(delta**2)**(0.5)
                sumx+= rpart(y2,delta)
                listy.append(sumx)
            else :
                return listx,listy,sumx
def twhole(N,a,b):
    listx=np.linspace(a,b,N)
    listy=[]
    sumx=0
    for x in range(0,N-1):
        y1=function(listx[x])
        y2=function(listx[x+1])
        delta=listx[x]-listx[x+1]
        delta=(delta**2)**(0.5)
        sumx+= tpart(y1,y2,delta)
        listy.append(sumx)    
    return listx,listy,sumx    
#this evaluates the trapezoidal rule with end corrections
def twhole2(N,a,b):
    listx=np.linspace(a,b,N)
    delta=listx[0]-listx[1]
    listy=[]
    sumx=0
    A=fderiv(a)
    B=fderiv(b)
    sumx-=((delta**2)/12.0)*(B-A)
    for x in range(0,N):
        if(x<N-1):
            y1=function(listx[x])
            y2=function(listx[x+1])
            delta=(delta**2)**(0.5)
            sumx+= tpart(y1,y2,delta)
            listy.append(sumx)
        else :
            return listx,listy,sumx   

     
def swhole(N,a,b):
    listx=np.linspace(a,b,N)
    delta=listx[0]-listx[1]
    listy=[]
    sumx=0
    for x in range(1,int(N/2)):
        y1=function(listx[2*x-2])
        y2=function(listx[2*x-1])
        y3=function(listx[2*x])
        delta=(delta**2.0)**(0.5)
        sumx+= spart(y1,y2,y3,delta)
        listy.append(sumx)
    return listx,listy,sumx

def rhomberg(N,a,b,steps):
    L=2**N
    h=(float(b)-(a))/N
    A=zeros(2**N)
    B=zeros(2**N,1)
    print("We are currently at bin= "+ str(b))
    for x in range(0,L):
        for y in range(0,L):
            if y==0:
                A[x,y]=1.0
                n=(2**x)*steps
                print("row= "+str(x) +" has this many steps "+ str(n))
                B[x,0]=swhole(int(n),a,b)[2]
                
            else:
                A[x,y]=-(h/(2**x))**(2*y)
    System=(A.copy()).col_insert((L),B)
    x=symbols('a0:%d'%(L),Real=True)
    b=solve_linear_system(System,*x)
    
    evals=0
    i=N
    while i>0:
        evals= 2**(i)+evals
        i=i-1
    ans=[b[x[0]],b[x[L-1]],evals]
    
    return ans
    

def rhombergwhole(a,b,step,error):
    bins=np.linspace(a,b,step)
    x=[]
    y=[]
    evals=[]
    sumy=0;
    for i in range(0,len(bins)-1):
        exitwhile=False
        locala=bins[i]
        localb=bins[i+1]
        N=1 
        while( not exitwhile):
            ans=rhomberg(N,locala,localb,step)
            #print("this is the N value "+str(N))
            #print("this is the error " + str(ans[1]))
            if(ans[1]<error):
                exitwhile=True
            if(N>2):
                exitwhile=True
            N=N+1
        evals.append(ans[2])
        sumy=sumy+float(ans[0])
        x.append(bins[i])
        y.append(sumy)
    return x,y,evals
    
    