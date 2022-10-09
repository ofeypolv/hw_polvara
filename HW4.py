import numpy as np
import astropy.constants as ac

tol = 1e-15
G = ac.G.value
M = ac.M_earth.value
m = 7.34767309e22
om = 2.662e-6
R = 3.844e8

np.seterr(divide='ignore')


def lagrpt(x):
    return G*M/(x**2) - G*m/((R-x)**2) - (om**2)*x

def der(f,x):
    h=1e-5
    return (f(x+(h/2))-f(x-(h/2)))/h

def newton(f, x, tol):
    while abs(f(x)) > tol:
        Dx = f(x)/der(f,x)
        x2 = x - Dx
        x = x2
    return x

def secant(f, x1, x2, tol):
    xm, x0, c = 0, 0, 0
    if (f(x1) * f(x2) < 0):
        while True:
            x0 = ((x1*f(x2) - x2*f(x1))/(f(x2) - f(x1)))
            c = f(x1) * f(x0)
            x1 = x2
            x2 = x0
            if (c == 0):
                break
            xm = ((x1*f(x2) - x2*f(x1))/(f(x2) - f(x1)))
            if (abs(xm - x0) < tol):
                break
        return x0
 
print("The Earth-Moon Lagrangian point L1 computed with the Newton method is {:e} m".format(newton(lagrpt,R/2,tol)))
print("The Earth-Moon Lagrangian point L1 computed with the secant method is {:e} m".format(secant(lagrpt,R/2,100*R/99,tol)))