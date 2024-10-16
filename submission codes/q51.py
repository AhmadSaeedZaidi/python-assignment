import numpy as np
import plotly.graph_objects as go

# Define ranges for x and y
x = np.linspace(-3, 3, 800)  # x-axis limits
y = np.linspace(-3, 3, 800)  # y-axis limits

# Create a meshgrid for x and y
x, y = np.meshgrid(x, y)

# Calculate corresponding z values for the surface
z = x**2 + y**2

# Create the surface plot
surface = go.Surface(x=x, y=y, z=z, colorscale='Blues', opacity=1.0, showscale=True)

# Create the figure
fig = go.Figure(data=[surface])

# Labels, title, and adjust axis limits
fig.update_layout(scene=dict(
                    xaxis=dict(title='X Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-3, 3]),  # x-axis limits
                    yaxis=dict(title='Y Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[-3, 3]),  # y-axis limits
                    zaxis=dict(title='Z Axis', titlefont=dict(color='black'), 
                               showbackground=False, 
                               color='black', 
                               gridcolor='gray', 
                               zerolinecolor='black',
                               range=[0, 8]),  # z-axis limits (max value is when x and y are both 3)
                  ),
                  title='Surface: z = x² + y²',
                  plot_bgcolor='white')

# Show plot
fig.show()
