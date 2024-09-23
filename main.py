import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 2 * np.pi, 100)

# Parametric equations x(t) and y(t)
x = np.cos(t)
y = np.sin(t)

# Plotting the parametric curve
plt.plot(x, y)
plt.xlabel('x(t)')
plt.ylabel('y(t)')
plt.title('Parametric Plot of a Circle')
plt.gca().set_aspect('equal')  # Set equal scaling for x and y axes
plt.grid(True)
plt.show()
