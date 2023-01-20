import plotly.graph_objects as go

# Get cuboid dimensions from user
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

# Create the x, y, and z coordinates of each vertex of the cuboid
x = [length/2, length/2, -length/2, -length/2, length/2, length/2, -length/2, -length/2]
y = [width/2, width/2, width/2, width/2, -width/2, -width/2, -width/2, -width/2]
z = [0, height, height, 0, 0, height, height, 0]

# Create the 3D cuboid
fig = go.Figure(data=[go.Mesh3d(x=x,
                                y=y,
                                z=z,
                                i=[0,1,2,3,4,5,6,7],
                                j=[1,2,3,0,5,6,7,4],
                                k=[0,1,2,3,4,5,6,7],
                                color='blue')])

# Update the layout of the figure
fig.update_layout(scene = dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z',))

fig.show()

