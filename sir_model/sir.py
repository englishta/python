import math
import matplotlib.pyplot as plt

N = 1000000
x = N-10
y = 10
z = 0

taxis = []
xaxis = []
yaxis = []
zaxis = []

beta = 0.2/N
gamma = 0.07
dt = 0.001

t = 0
cnt = 0
while t < 180:
    if cnt%100 == 0:
        taxis.append(t)
        xaxis.append(x)
        yaxis.append(y)
        zaxis.append(z)
# step 1
    kx1 = -beta*x*y
    ky1 = beta*x*y - gamma*y
# step 2
    t2 = t+dt
    x2 = x+kx1*dt
    y2 = y+ky1*dt
    kx2 = -beta*x2*y2
    ky2 = beta*x2*y2 - gamma*y2
# update
    x = x+(kx1+kx2)*dt/2
    y = y+(ky1+ky2)*dt/2
    z = N-x-y
    t = t+dt
    cnt+=1

plt.title("SIR MODEL")
plt.plot(taxis,xaxis, color=(0.0,1,0.0), linewidth=1.0, label='S')
plt.plot(taxis,yaxis, color=(1.0,0,0.0), linewidth=1.0, label='I')
plt.plot(taxis,zaxis, color=(0.0,0,1.0), linewidth=1.0, label='R')
plt.xlim(0,180)
plt.legend()
plt.xlabel('DAY')
plt.ylabel('X, Y, Z')
plt.grid(True)
