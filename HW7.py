import numpy as np
from scipy import integrate

#weight function w(x)
def fw(x):
    return x**(-1/2)

#probability distro p(x)
def fp(x):
    return 1/(2*x**(1/2))

#probability distro p(x) after transformation formula
def pdistro():
    return (np.random.random())**2

#original integrand f(x), divergent
def fint(x):
    return (x**(-1/2))/(1+np.exp(x))

#non-divergent integrand g(x)
def gint(x):
    return 1/(1+np.exp(x))

N = 1000000
I = 0
wint = (integrate.quad(lambda x: fw(x), 0, 1)[0])
for i in range(N):
    x = pdistro()
    I += 2*gint(x)/N #integral(w(x))=2

print("The pdf p(x) is obtained from the weight w(x) as w(x)/integral(w(x)), where integral(w(x))=2 bw 0 and 1")
print("The transformation formula for p(x) is x(z)=z^2, with z uniform random number bw 0 and 1")
print("The integral computed with Monte Carlo with importance sampling is {}".format(I))
print("The integral computed with scipy is {}".format(integrate.quad(lambda x: fint(x), 0, 1)[0]))