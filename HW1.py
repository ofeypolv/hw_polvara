import numpy as np
import matplotlib.pyplot as plt

#EX 3.2

fig,axis = plt.subplots(nrows=1,ncols=3)
plt.subplots_adjust(hspace=0.5,wspace=0.5)

#PART 1 - DELTOID CURVE
t1 = np.linspace(0,2*np.pi)
x1 = 2*np.cos(t1)+np.cos(2*t1)
y1 = 2*np.sin(t1)-np.sin(2*t1)
axis[0].plot(x1,y1)
axis[0].set_xlabel("x")
axis[0].set_ylabel("y")
axis[0].set_title("Deltoid Curve")


#PART 2 - GALILEAN SPIRAL
t2 = np.linspace(0,10*np.pi,1000)
r2 = (t2)**2
x2 = r2*np.cos(t2)
y2 = r2*np.sin(t2)
axis[1].plot(x2,y2)
axis[1].set_xlabel("x")
axis[1].set_ylabel("y")
axis[1].set_title("Galilean Spiral")


#PART 3 - FEY'S FUNCTION
t3 = np.linspace(0,24*np.pi,10000)
r3 = np.exp(np.cos(t3)) - 2*np.cos(4*t3) + (np.sin(t3/12))**5
x3 = r3*np.cos(t3)
y3 = r3*np.sin(t3)
axis[2].plot(x3,y3)
axis[2].set_xlabel("x")
axis[2].set_ylabel("y")
axis[2].set_title("Fey's Function")


plt.show()


