import numpy as np
import plotly.graph_objects as go

# Define ranges for y and z with increased limits
y = np.linspace(-2, 2, 800)  # Adjusted range for better visibility
z = np.linspace(-5, 5, 800)  # Further increased range for z

# Create a meshgrid for y and z
y, z = np.meshgrid(y, z)

# Calculate corresponding x values
x = 4 - 4 * y**2 - z**2

# Create the surface plot
surface = go.Surface(x=x, y=y, z=z, colorscale='Blues', opacity=1.0, showscale=True)

# Figure plot
fig = go.Figure(data=[surface])

# Labels, title, and adjust axis limits
fig.update_layout(scene=dict(
                    xaxis=dict(title='X Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-10, 10]), # x-axis limits
                    yaxis=dict(title='Y Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-2, 2]), # y-axis limits
                    zaxis=dict(title='Z Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-5, 5]), # z-axis limits
                  ),
                  title='Surface: x = 4 - 4y² - z² (Light Mode)',
                  plot_bgcolor='white')

# Show plot
fig.show()
