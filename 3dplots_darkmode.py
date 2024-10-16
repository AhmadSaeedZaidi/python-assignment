import numpy as np
import plotly.graph_objects as go

# Define a range for the parameter theta and phi
theta = np.linspace(0, 2 * np.pi, 1000)  # bounds , and number of points for the theta parameter
phi = np.linspace(0, np.pi, 1000)  # bounds , and number of points for phi parameter

# Create a meshgrid for theta and phi
theta, phi = np.meshgrid(theta, phi)

# convert the equation to parametric
x = 2 * np.sin(phi) * np.cos(theta)  # (2) = sqrt(36/9) -> scaling for x
y = 3 * np.sin(phi) * np.sin(theta)  # (3) = sqrt(36/4) -> scaling for y
z = np.cos(phi)  # 1 = sqrt(36/36) -> scaling for z

# surface plot for the continuous ellipsoid
surface = go.Surface(x=x, y=y, z=z, colorscale='Plasma', opacity=0.8, showscale=True)

# figure plot
fig = go.Figure(data=[surface])

# labels, title, and adjust axis limits
# each dictionary has parameters to make the axis more visible
fig.update_layout(scene=dict(
                    xaxis=dict(title='X Axis', titlefont=dict(color='white'), 
                               showbackground=False, 
                               color='white', 
                               gridcolor='darkgray', 
                               zerolinecolor='white',
                               range=[-2, 2]), #  x-axis limits
                    yaxis=dict(title='Y Axis', titlefont=dict(color='white'), 
                               showbackground=False, 
                               color='white', 
                               gridcolor='darkgray', 
                               zerolinecolor='white',
                               range=[-3, 3]), #  y-axis limits
                    zaxis=dict(title='Z Axis', titlefont=dict(color='white'), 
                               showbackground=False, 
                               color='white', 
                               gridcolor='darkgray', 
                               zerolinecolor='white',
                               range=[-1, 1]), #  z-axis limits
                  ),
                  title='Ellipsoid: 9x² + 4y² + 36z² = 36 (Dark Mode)',
                  plot_bgcolor='black')

# Show plot
fig.show()
