import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def sir_model(v, t, beta, gamma):
    x = v[0]
    y = v[1]
    z = v[2]
    dxdt = - beta*x*y
    dydt = beta*x*y - gamma*y
    dzdt = gamma*y
    return [dxdt, dydt, dzdt]

N = 1000000
beta=0.2/N
gamma=0.07
dt=0.1

init_vals=[N-10, 10, 0]
times = np.arange(0.0, 180, dt)
args=(beta, gamma)
results = odeint(sir_model, init_vals, times, args=args)

plt.title("SIR MODEL")
plt.plot(times[::10],results[::10,0], color=(0.0,1,0.0), linewidth=1.0, label='S')
plt.plot(times[::10],results[::10,1], color=(1.0,0,0.0), linewidth=1.0, label='I')
plt.plot(times[::10],results[::10,2], color=(0.0,0,1.0), linewidth=1.0, label='R')

plt.xlim(0,180)
plt.legend()
plt.xlabel('DAY')
plt.ylabel('X, Y, Z')
plt.grid(True)
plt.show()
