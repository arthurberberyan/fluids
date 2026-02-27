import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams.update({
"font.family": "STIXGeneral",
"mathtext.fontset": "stix",
"font.size": 14,
"axes.linewidth": 1.2,
"xtick.direction": "in",
"ytick.direction": "in",
"xtick.top": True,
"ytick.right": True
})


N = 200 # total grid points 
steps =10 # adjust this to control the speed of the animation (10 vs 100)
r_min = 0.01 
r_max = 10.0 
y_min = 0.0
y_max = 1.0
r = np.linspace(r_min, r_max, N) # make r into an array
dr = r[1] - r[0] 
nu = 2.0 # viscosity 
dt = 0.0001 # time step, needs to be small so the animation plays longer



u = -(9* nu) / (2*r) # inward advection 
diff = 3*nu # simplified diffusion coefficient
beta = diff*dt / dr**2 # saw the usage of beta for diffusion, AI helped here

# initial Gaussian
r0 = 0.5*(r_min + r_max) # surface density to have centered
sigma = np.exp(-0.5*((r - r0) / (0.10*(r_max - r_min)))**2) # simplified Gaussian

# boundary conditions
# surface density 0 = surface density 1; surface density N-1 = surface density N-2
def boundary(s):
    s[0] = s[1]
    s[-1] = s[-2]

# diffusion matrix, AI helped here
n = N - 2
A = (1 + 2*beta)*np.eye(n) - beta*np.eye(n, k=1) - beta*np.eye(n, k=-1)

def solve(s):
    # Eve reccomends to use.copy() since we will modify here
    advec = s.copy()

    # diffusion 
    # solves linear system
    s[1:-1] = np.linalg.solve(A, advec[1:-1])
    boundary(s)

    # Lax–Friedrichs advection, AI helped here
    advec[1:-1] = 0.5*(s[2:] + s[:-2]) - (u[1:-1]*dt/(2*dr))*(s[2:] - s[:-2])
    boundary(advec)
    return advec

fig, ax = plt.subplots()
sigma_plot = ax.plot(r, sigma)[0]
ax.set_xlabel(r"$r$")
ax.set_ylabel(r"$\Sigma$")
ax.set_xlim(r_min, r_max)
ax.set_ylim(y_min, y_max)

t = [0.0]
def plot(p):
    for p in range(steps):
        sigma[:] = solve(sigma)
        t[0] += dt
    sigma_plot.set_ydata(sigma)
    return sigma_plot

animation = FuncAnimation(fig, plot, interval=50, cache_frame_data=False)
plt.show()