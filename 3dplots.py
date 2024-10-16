import numpy as np
import plotly.graph_objects as go

# Define a range for the parameter theta and x
theta = np.linspace(0, 2 * np.pi, 1000)  # bounds , and number of points for the theta parameter
x = np.linspace(-10, 10, 1000)  # bounds , and number of points for X axis

# Create a meshgrid for x and theta
x, theta = np.meshgrid(x, theta)

# convert the equation to parametric
y = (4/3) * np.sin(theta)  # (4/3) = sqrt(16/9) -> scaling for y
z = 4 * np.cos(theta)      # 4 = sqrt(16) -> scaling for z

# surface plot for the continuous elliptical cylinder
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
                               range=[-10, 10]), #  x-axis limits
                    yaxis=dict(title='Y Axis', titlefont=dict(color='white'), 
                               showbackground=False, 
                               color='white', 
                               gridcolor='darkgray', 
                               zerolinecolor='white',
                               range=[-5, 5]), #  y-axis limits
                    zaxis=dict(title='Z Axis', titlefont=dict(color='white'), 
                               showbackground=False, 
                               color='white', 
                               gridcolor='darkgray', 
                               zerolinecolor='white',
                               range=[-5, 5]), #  z-axis limits
                  ),
                  title='Elliptical Cylinder: 9y² + z² = 16',
                  plot_bgcolor='black')

# Show plot
fig.show()
