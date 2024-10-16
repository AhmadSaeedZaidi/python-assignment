import numpy as np
import plotly.graph_objects as go

# Define a range for the parameter theta and phi
theta = np.linspace(0, 2 * np.pi, 800)  # Increased number of points for better resolution
phi = np.linspace(0, np.pi, 800)

# Create a meshgrid for theta and phi
theta, phi = np.meshgrid(theta, phi)

# Convert the equation to parametric
x = 2 * np.sin(phi) * np.cos(theta)  # (2) = sqrt(36/9) -> scaling for x
y = 3 * np.sin(phi) * np.sin(theta)  # (3) = sqrt(36/4) -> scaling for y
z = np.cos(phi)  # 1 = sqrt(36/36) -> scaling for z

# Create the negative z values for the lower half
z_neg = -np.cos(phi)

# Create surface plots for the upper and lower halves
surface_upper = go.Surface(x=x, y=y, z=z, colorscale='Blues', opacity=1.0, showscale=True)
surface_lower = go.Surface(x=x, y=y, z=z_neg, colorscale='Blues', opacity=1.0, showscale=False)

# Figure plot
fig = go.Figure(data=[surface_upper, surface_lower])

# Labels, title, and adjust axis limits
fig.update_layout(scene=dict(
                    xaxis=dict(title='X Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-2, 2]), # x-axis limits
                    yaxis=dict(title='Y Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-3, 3]), # y-axis limits
                    zaxis=dict(title='Z Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-1, 1]), # z-axis limits
                  ),
                  title='Ellipsoid: 9x² + 4y² + 36z² = 36 (Improved Visibility)',
                  plot_bgcolor='white')

# Show plot
fig.show()
