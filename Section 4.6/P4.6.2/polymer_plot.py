# Compare the observed distribution of end-to-end distances for Np random-
# flight polymers with the predicted probability distribution function.

import math
import numpy as np
import matplotlib.pyplot as plt
from polymer import Polymer
pi = np.pi

# Calculate R for Np polymers
Np = 3000
# Each polymer consists of N segments of length a
N, a = 1000, 1.
R = [None] * Np
for i in range(Np):
    polymer = Polymer(N, a)
    Rx, Ry, Rz = polymer.R
    R[i] = np.sqrt(Rx**2 + Ry**2 + Rz**2)
    # Output a progress indicator every 100 polymers
    if not (i+1) % 100:
        print(i+1)

# Plot the distribution of Rx as a normalized histogram
# using 50 bins
plt.hist(R, 50)

# Plot the theoretical probability distribution, Pr, as a function of r
r = np.linspace(0,200,1000)
msr = N * a**2
Pr = 5000.0 * 4.0*pi*r**2 * (2 * pi * msr / 3)**-1.5 * np.exp(-3*r**2 / 2 / msr)
plt.plot(r, Pr, lw=2, c='r')
plt.xlabel('R')
plt.ylabel('P(R)')
plt.show()

polymer.save_SVG()