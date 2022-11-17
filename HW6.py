import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import animation

L = 101
N = int(1e5) #program slows down for N=1e6, so I'm considering N=1e5
steps = np.array([[0.5,0],[-0.5,0],[0,0.5],[0,-0.5]])
locations = np.zeros((1,2))

for n in range(N-1):
    if (abs(locations[-1][0]) < L/2) and (abs(locations[-1][1]) < L/2):
        nextloc = [locations[-1] + steps[random.randrange(4)]]
        locations = np.append(locations, nextloc, axis=0)
    #sides boundary conditions
    elif (locations[-1][0] == L/2) and (abs(locations[-1][1]) < L/2): #right side
        nextloc = [locations[-1] + np.delete(steps,0,axis=0)[random.randrange(3)]]
        locations = np.append(locations, nextloc, axis=0)
    elif (locations[-1][0] == -L/2) and (abs(locations[-1][1]) < L/2): #left side
        nextloc = [locations[-1] + np.delete(steps,1,axis=0)[random.randrange(3)]]
        locations = np.append(locations, nextloc, axis=0)
    elif (abs(locations[-1][0]) < L/2) and (locations[-1][1] == L/2): #top side
        nextloc = [locations[-1] + np.delete(steps,2,axis=0)[random.randrange(3)]]
        locations = np.append(locations, nextloc, axis=0)
    elif (abs(locations[-1][0]) < L/2) and (locations[-1][1] == -L/2): #bottom side
        nextloc = [locations[-1] + np.delete(steps,3,axis=0)[random.randrange(3)]]
        locations = np.append(locations, nextloc, axis=0)
    #edges boundary conditions
    elif (locations[-1][0] == L/2) and (locations[-1][1] == L/2): #top right corner
        nextloc = [locations[-1] + np.delete(steps,[0,2],axis=0)[random.randrange(2)]]
        locations = np.append(locations, nextloc, axis=0)
    elif (locations[-1][0] == -L/2) and (locations[-1][1] == L/2): #top left corner
        nextloc = [locations[-1] + np.delete(steps,[1,2],axis=0)[random.randrange(2)]]
        locations = np.append(locations, nextloc, axis=0)
    elif (locations[-1][0] == -L/2) and (locations[-1][1] == -L/2): #bottom left corner
        nextloc = [locations[-1] + np.delete(steps,[1,3],axis=0)[random.randrange(2)]]
        locations = np.append(locations, nextloc, axis=0)
    elif (locations[-1][0] == L/2) and (locations[-1][1] == -L/2): #bottom right corner
        nextloc = [locations[-1] + np.delete(steps,[0,3],axis=0)[random.randrange(2)]]
        locations = np.append(locations, nextloc, axis=0)

xdata = locations[:,0]
ydata = locations[:,1]
print(len(locations))

fig, ax = plt.subplots(figsize=(8,8))
ax.set_xlim(-L/2,L/2)
ax.set_ylim(-L/2,L/2)
line, = ax.plot([], [], lw=2)
line.set_color('blue')
def animate(i):
    line.set_data(xdata[:i], ydata[:i])
    return line

anim = animation.FuncAnimation(fig, animate)
#save as a gif
#writergif = animation.PillowWriter(fps=30)
#anim.save('2drandomwalk.gif',writer=writergif)
plt.title("2D discrete Brownian Motion")
plt.show()