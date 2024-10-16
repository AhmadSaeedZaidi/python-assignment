import numpy as np
import matplotlib.pyplot as plt

# Define the parameter t
t = np.linspace(0, 8 * np.pi, 1000000000)

# Parametric equations x(t) and y(t)
x = np.log(t)
y = 3*np.e**(-t/2)

# Plotting the parametric curve
plt.plot(x, y)
plt.xlabel(r'x = ln(t)')
plt.ylabel(r'y = 3 $e^{-\frac{t}{2}}$')
plt.title('Parametric Plot')
plt.gca().set_aspect('equal')  # Set equal scaling for x and y axes
plt.grid(True)
plt.show()
