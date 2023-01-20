import plotly.graph_objects as go

# Get pyramid dimensions from user
base = float(input("Enter the base of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

# Create the x, y, and z coordinates of each vertex of the pyramid
x = [base/2, -base/2, -base/2, base/2, 0]
y = [base/2, base/2, -base/2, -base/2, 0]
z = [0, 0, 0, 0, height]

# Create the 3D pyramid
fig = go.Figure(data=[go.Mesh3d(x=x,
                                y=y,
                                z=z,
                                i=[0,1,2,3],
                                j=[1,2,3,0],
                                k=[4,4,4,4],
                                color='orange')])

# Update the layout of the figure
fig.update_layout(scene = dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'))

fig.show()

