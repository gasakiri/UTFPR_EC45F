"""
Gabriel Augusto Morisaki Rita
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

"""
Exercício 1
"""

dt = 0.01
t = np.arange(start=-2, stop=2 + dt, step=dt)

# 1 - p(t) = exp(2*t)
p = np.exp(2 * t)
dp = np.gradient(p, t)
plt.plot(t, dp)
plt.show()