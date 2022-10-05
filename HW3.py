import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import scipy.constants as sc

e0 = sc.epsilon_0
k = 1./(4.*np.pi*e0) #coulomb constant

#function that compute potential at point (x,y) for a single point charge q located at qd 
def compute_potential(q, qd, x, y):
    X, Y = np.meshgrid(x, y)
    r = np.sqrt((X - qd[0])**2 + (Y - qd[1])**2)
    potential = k*q/r
    return potential

#function that compute field x,y components at point (x,y) for a single point charge q located at qd 
def compute_field(q, qd, x, y):
    h = 1e-5
    #EX = -(np.gradient(compute_potential(q, qd, x, y),x,axis=1))
    #EY = -(np.gradient(compute_potential(q, qd, x, y),y,axis=0))
    EX = - (compute_potential(q,qd,x+(h/2),y) - compute_potential(q,qd,x-(h/2),y))/h #Ex=-dV/dx
    EY = - (compute_potential(q,qd,x,y+(h/2)) - compute_potential(q,qd,x,y-(h/2)))/h #Ey=-dV/dy
    return EX,EY

#grid
Nx = 100
Ny = 100
x = np.linspace(-0.5, 0.5, Nx)
y = np.linspace(-0.5, 0.5, Ny)

#charges (q, (qx,qy))
charges = []
charges.append((-1, (-0.05, 0)))
charges.append((1, (0.05, 0)))

#overall potential + x,y field computation
potential = np.zeros((Nx,Ny))
Ex = np.zeros((Nx,Ny))
Ey = np.zeros((Nx,Ny))
for charge in charges:
    pot = compute_potential(*charge, x, y)
    potential += pot
    ex, ey = compute_field(*charge,x,y)
    Ex += ex
    Ey += ey

#plots
fig,axis = plt.subplots(nrows=1,ncols=2,figsize=(10, 5))

#potential color plot
im0 = axis[0].pcolormesh(x, y, potential)
axis[0].set_xlabel("x")
axis[0].set_ylabel("y")
axis[0].set_title("Electric potential")
fig.colorbar(im0, ax=axis[0])

#field lines plot with charges drawing
axis[1].streamplot(x,y,Ex,Ey)
axis[1].set_xlabel("x")
axis[1].set_ylabel("y")
axis[1].set_title("Electric field")
chargeCols = {'Neg' : '#0000FF','Pos' : '#FF0000'}
circle1 = axis[1].add_artist(Circle((-0.05,0), 0.035, color = chargeCols['Neg'],label='-1'))
circle2 = axis[1].add_artist(Circle((0.05,0), 0.035, color = chargeCols['Pos'],label='+1'))
axis[1].add_patch(circle1)
axis[1].add_patch(circle2)
axis[1].legend(bbox_to_anchor=(1.05, 0.9))

fig.suptitle('Electric dipole', fontsize = 18)
plt.show()