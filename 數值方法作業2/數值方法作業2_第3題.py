# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 08:41:15 2025

@author: chung
"""
def f(x):
    y=-26+(85*x)-(91*x**2)+(44*x**3)-(8*x**4)+x**5
    return y

def df(x):
    y=85-(182*x)+(132*x**2)-(32*x**3)+(5*x**4)
    return y
def df2(x):
    y=-21-(20*x)-(63*x**2)+(44*x**3)+(5*x**4)
    return y
def bis(a,b):
    A=a
    B=b
    err=0.0001
    c=(A+B)/2
    while abs(f(c))>err:
        if f(c)<0 and f(A)<0:
            A=c
        else:
            B=c
        c=(A+B)/2
    return c
def falsepos(a,b):
    err=0.0001
    p0=a
    p1=b
    fp0=f(p0)
    fp1=f(p1)
    p2=p0-((p1-p0)*fp0)/(fp1-fp0)
    while abs(f(p2))>err:
        if f(p2)<0 and f(p1)<0:
            p1=p2
        else:
            p0=p2
        fp0=f(p0)
        fp1=f(p1)
        p2=p0-((p1-p0)*fp0)/(fp1-fp0)
    return p2
def newton(a):
    err=0.0001
    x0=a
    x1=x0-(f(x0)/df(x0))
    while abs(f(x1))>err:
        x0=x1
        x1=x0-(f(x0)/df(x0))
    return x1
def sec(a,b):
    err=0.0001
    x0=a
    x1=b
    x2=x1-(((x1-x0)*f(x1))/(f(x1)-f(x0)))
    while abs(f(x2))>err:
        x0=x1
        x1=x2
        x2=x1-(((x1-x0)*f(x1))/(f(x1)-f(x0)))
    return x2
def ste(a):
    err=0.0001
    p0=a
    p1=p0-(f(p0)/((f(p0+f(p0))/f(p0))-1))
    while abs(f(p1))>err:
      p0=p1
      p1=p0-(f(p0)/((f(p0+f(p0))/f(p0))-1))
    return p1

rootbis=bis(0,1)
print('Bisection method: '+str(rootbis))
rootfp=falsepos(0,1)
print('False-position method: '+str(rootfp))
rootnew=newton(0)
print('Newton’s method: '+str(rootnew))
rootsec=sec(0, 1)
print('Secant method: '+str(rootsec))
rootste=ste(0)
print('Steffensen’s method: '+str(rootste))
'''
newtonf(0)
def f2(x):
    y=-5-(21*x)-(10*x**2)-(21*x**3)+(11*x**4)+x**5
    return y

def newtonf(a):
    err=0.0001
    x0=a
    x1=x0-(f2(x0)/df2(x0))
    print('x0:'+str(x0))
    print('fx0:'+str(f2(x0)))
    print('fx0":'+str(df2(x0)))
    print('x1:'+str(x1))
    print('fx1:'+str(f2(x1)))
    print('fx1":'+str(df2(x1)))
    n=1
    while abs(f2(x1))>err:
        n=n+1
        x0=x1
        x1=x0-(f2(x0)/df2(x0))
        print('x'+str(n)+':'+str(x1))
        print('fx'+str(n)+':'+str(f2(x1)))
        print('fx'+str(n)+'":'+str(df2(x1)))
'''