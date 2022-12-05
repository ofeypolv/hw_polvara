import numpy as np
import matplotlib.pyplot as plt

#physical constants + parameters
ms = [0.25,0.5,1.,1.5,2.]
R = 0.08
rho = 1.22
C = 0.47
k = 0.5*np.pi*(R**2)*rho*C
g = 9.81

N = 100

#initial conditions
t0 = 0
x0 = 0
y0 = 0
v0 = 100
th0 = np.radians(30)
v0x = v0*np.cos(th0)
v0y = v0*np.sin(th0)

#max range + time for the non drag case (keep them for reference)
xg = 2*v0x*v0y/g
tg = 2*v0y/g

#u1=x, u2=xdot, u3=y, u4=ydot
def U(u,t,m):
    u1, u2, u3, u4 = u
    return np.asarray([u2,-(k/m)*np.sqrt(u2**2 + u4**2)*u2,u4,-g-(k/m)*np.sqrt(u2**2 + u4**2)*u4])

#mass dependent 4th order RK
def ode_RK4(f, u_0, t0, tf, N, m):
    h = (tf-t0)/N
    usol = [u_0]
    u = np.copy(u_0)
    tpoints = np.arange(t0,tf+h,h)
    for t in tpoints:
        k1 = h*f(u,t,m)
        k2 = h*f(u+0.5*k1,t+0.5*h,m)
        k3 = h*f(u+0.5*k2,t+0.5*h,m)
        k4 = h*f(u+k3,t+h,m)
        u = u + (k1+2*k2+2*k3+k4)/6
        usol.append(u)
    return usol

#plotting different trajectories + max ranges for different masses
ax = plt.subplot(111)

for mi in ms:
    u = ode_RK4(U, np.array([x0,v0x,y0,v0y]), t0, tg, N, mi)
    x = [a[0] for a in u]
    y = [a[2] for a in u]
    maxrange = x[np.argmin(np.abs(y[1:]))+1]
    print("The maximum range for m = {}kg is {}m".format(mi,round(maxrange,1)))
    ax.plot(x, y, label = "m = {}".format(mi))
    
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),title = "mass [kg]")
ax.axis([0, 400, 0, 80])
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.show()