import numpy as np
import math as mt
import matplotlib.pyplot as plt

a = 0.0

#EX 5.3

def f(t):
   return mt.exp(-(t**2))

#TRAPEZOID INTEGRAL AS A FUNCTION OF UPPER INTEGRATION EXTREMUM X
def int_t(x):
    N_t = 100
    h_t = (x-a)/N_t
    s_t = 0.5*f(a)+0.5*f(x)
    for k in range(1,N_t):
        s_t += f(a+k*h_t)
    return h_t*s_t

#SIMPSON INTEGRAL AS A FUNCTION OF UPPER INTEGRATION EXTREMUM X
def int_s(x):
    N_s = 100
    h_s = (x-a)/N_s
    s_s = (1/3)*f(a) + (1/3)*f(x)
    for k in range(1,int(N_s/2)):
        s_s += 4*f((2*k-1)*h_s)
    for k in range(1,int((N_s/2)-1)):
        s_s += 2*f((2*k)*h_s)
    return (h_s*s_s)/3

#TRAPEZOID INTEGRATION METHOD WAS CHOSEN
x = np.arange(0,3,0.1)
y = [int_t(i) for i in x]
plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()