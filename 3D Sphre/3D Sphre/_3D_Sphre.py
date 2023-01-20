import plotly.graph_objects as go
import numpy as np

# Get sphere radius from user
radius = float(input("Enter the radius of the sphere: "))

# Define the number of points to create the sphere
n = 50

# Create the x, y, and z coordinates of each point on the sphere
theta, phi = np.linspace(0, 2*np.pi, n), np.linspace(0, np.pi, n)
THETA, PHI = np.meshgrid(theta, phi)
x = radius * np.sin(PHI) * np.cos(THETA)
y = radius * np.sin(PHI) * np.sin(THETA)
z = radius * np.cos(PHI)

# Create the 3D sphere
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

# Update the layout of the figure
fig.update_layout(scene = dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'))

fig.show()

