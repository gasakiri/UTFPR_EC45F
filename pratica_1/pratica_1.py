"""
Gabriel Augusto Morisaki Rita
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pdf = PdfPages("python_pratica_1.pdf")

"""
Exercicio 1
"""

dt = 0.01
t = np.arange(start=-10, stop=10 + dt, step=dt)

# 1 - p(t) = sin(3t)
p = np.sin(3 * t)

# 2 - f(t) = exp(-t)
f = np.exp(-t)

# 3 - m(t) = t*exp(-t)
m = t * np.exp(-t)

# 4 - q(t) = exp(-t)*cos(t)
q = np.exp(-t) * np.cos(t)

functions = f"""
Exercicio 1

1. p(t) = sin(3t)
2. f(t) = exp(-t)
3. m(t) = t * exp(-t)
4. q(t) = exp(-t) * cos(t)

dt = 0.01
t = np.arange(start=-10, stop=10 + dt, step=dt)

p = np.sin(3 * t)

f = np.exp(-t)

m = t * np.exp(-t)

q = np.exp(-t) * np.cos(t)
"""
fig, ax = plt.subplots(figsize=(8.27, 11.69))
ax.text(0.5, 0.5, functions, fontsize=12, ha="center", va="center", wrap=True)
ax.set_axis_off()
pdf.savefig(fig)
plt.close(fig)

"""
Exercicio 2
"""

dt = 0.01
t = np.arange(start=-10, stop=10 + dt, step=dt)
u = np.zeros(t.size)
u = np.heaviside(t, 1)

p = np.sin(3 * t)  # 1 - p(t) = sin(3t)

f = np.multiply(np.exp(-t), u)  # 2 - f(t) = exp(-t)*u(t)

m = np.multiply(t, np.exp(-t))  # 3 - m(t) = t*exp(-t)

q = np.exp(-t) * np.cos(t) * u  # 4 - q(t) = exp(-t)*cos(t)*u(t)

functions = f"""
Exercicio 2

1. p(t) = sin(3t)
2. f(t) = exp(-t) * u(t)
3. m(t) = t * exp(-t)
4. q(t) = exp(-t) * cos(t) * u(t)

dt = 0.01
t = np.arange(start=-10, stop=10 + dt, step=dt)
u = np.zeros(t.size)
u = np.heaviside(t, 1)

p = np.sin(3 * t)

f = np.multiply(np.exp(-t), u)

m = np.multiply(t, np.exp(-t))

q = np.exp(-t) * np.cos(t) * u
"""
fig, ax = plt.subplots(figsize=(8.27, 11.69))
ax.text(0.5, 0.5, functions, fontsize=12, ha="center", va="center", wrap=True)
ax.set_axis_off()
pdf.savefig(fig)
plt.close(fig)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(t, p)
axs[0, 0].set_title("p(t) = sin(3t)")
axs[0, 0].set_xlabel("t")
axs[0, 0].set_ylabel("p(t)")
axs[0, 0].grid()

axs[0, 1].plot(t, f)
axs[0, 1].set_title("f(t) = exp(-t) * u(t)")
axs[0, 1].set_xlabel("t")
axs[0, 1].set_ylabel("f(t)")
axs[0, 1].grid()

axs[1, 0].plot(t, m)
axs[1, 0].set_title("m(t) = t * exp(-t)")
axs[1, 0].set_xlabel("t")
axs[1, 0].set_ylabel("m(t)")
axs[1, 0].grid()

axs[1, 1].plot(t, q)
axs[1, 1].set_title("q(t) = exp(-t) * cos(t) * u(t)")
axs[1, 1].set_xlabel("t")
axs[1, 1].set_ylabel("q(t)")
axs[1, 1].grid()

plt.tight_layout()
pdf.savefig(fig)
plt.close(fig)

pdf.close()
