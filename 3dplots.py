import numpy as np
import plotly.graph_objects as go

# Define a range for the parameter theta and x
theta = np.linspace(0, 2 * np.pi, 1000)  # Parameter for the ellipse (around the cylinder)
x = np.linspace(-10, 10, 1000)  # bounds , and number of points for 

# Create a meshgrid for x and theta
x, theta = np.meshgrid(x, theta)

# Parametric equations for the elliptical cylinder
y = (4/3) * np.sin(theta)  # (4/3) factor comes from sqrt(16/9) -> scaling for y
z = 4 * np.cos(theta)      # The z values follow from the equation of the ellipse

# Create a surface plot for the continuous elliptical cylinder
surface = go.Surface(x=x, y=y, z=z, colorscale='Plasma', opacity=0.8, showscale=True)

# Create the figure
fig = go.Figure(data=[surface])

# Set labels, title, and adjust axis limits
fig.update_layout(scene=dict(
                    xaxis_title='X Axis',
                    yaxis_title='Y Axis',
                    zaxis_title='Z Axis',
                    xaxis=dict(range=[-10, 10]),  # Increase x-axis limits
                    yaxis=dict(range=[-5, 5]),    # Increase y-axis limits
                    zaxis=dict(range=[-5, 5])     # Increase z-axis limits
                  ),
                  title='Elliptical Cylinder: 9y² + z² = 16 (Single Continuous Surface)')

# Show the plot
fig.show()
