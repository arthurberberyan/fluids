
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import iv  # needed for modified Bessel function

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

# ranges and parameters
x = np.linspace(0.1, 10.0, 1000)
taus = [0.01, 0.05, 0.1, 0.5, 1.0]

# function for viscous disk surface density
def visc_disk(x, tau):
    return (1.0/(tau * x**0.25)) * np.exp(-(1.0 + x**2)/tau) * iv(0.25, 2.0*x/tau)

fig, ax = plt.subplots()
# plot the curves for different tau values
for i in taus:
    y = visc_disk(x, i)
    ax.plot(x, y, label=fr"$\tau={i}$")


ax.set_xlabel("x")
ax.set_ylabel(r"$\Sigma \ (m/ \pi R_0^2)$")
ax.set_ylim(0, 3.0)
ax.set_xlim(0.1, 3.0)
ax.set_title("github.com/arthurberberyan/fluids")
ax.legend()
#fig.savefig("ps3_q1.png", dpi=300) 
plt.show()
