import numpy as np
import plotly.graph_objects as go

# Define ranges for theta and phi
theta = np.linspace(0, 2 * np.pi, 800)  # Angular coordinate
phi = np.linspace(-2, 2, 800)            # Radial coordinate

# Create a meshgrid for theta and phi
theta, phi = np.meshgrid(theta, phi)

# Parametric equations for the hyperboloid (a = b = c = 1)
x = np.cosh(phi) * np.cos(theta)
y = np.cosh(phi) * np.sin(theta)
z = np.sinh(phi)

# Create the surface plot
surface = go.Surface(x=x, y=y, z=z, colorscale='Viridis', opacity=1.0, showscale=True)

# Create the figure
fig = go.Figure(data=[surface])

# Labels, title, and adjust axis limits
fig.update_layout(scene=dict(
                    xaxis=dict(title='X Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-5, 5]),  # Adjusted x-axis limits
                    yaxis=dict(title='Y Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-5, 5]),  # Adjusted y-axis limits
                    zaxis=dict(title='Z Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-5, 5]),  # Adjusted z-axis limits
                  ),
                  title='Hyperboloid of One Sheet (Light Mode)',
                  plot_bgcolor='white')

# Show plot
fig.show()
