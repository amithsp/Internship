import plotly.graph_objects as go

# Get cube dimensions from user
side = float(input("Enter the side of the cube: "))
#side = float(input("Enter the side of the cube: "))
#side = float(input("Enter the side of the cube: "))



# Create a 3D cube in plotly
fig = go.Figure(data=[go.Mesh3d(x=[0,side,side,0,0,side,side,0],
                   y=[0,0,side,side,0,0,side,side],
                   z=[0,0,0,0,side,side,side,side],
                   i=[7,0,0,0,4,4,6,6,4,0,3,2],
                   j=[3,4,1,2,5,6,5,2,0,1,6,3],
                   k=[0,7,2,3,6,7,1,1,5,5,7,6],
                   color='lightpink')])

# Update the layout of the figure
fig.update_layout(scene = dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z'))

fig.show()
