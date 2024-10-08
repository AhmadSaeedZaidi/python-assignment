import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 8 * np.pi, 1000)

# Parametric equations x(t) and y(t)
x = np.sqrt(t)
y = np.sqrt(t)*np.cos(t)

# Plotting the parametric curve
plt.plot(x, y)
plt.xlabel(r'x = $\sqrt{t}$')
plt.ylabel(r'y = $\sqrt{t}$ cos(t)')
plt.title('Parametric Plot')
plt.gca().set_aspect('equal')  # Set equal scaling for x and y axes
plt.grid(True)
plt.show()
