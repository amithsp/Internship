import pyrender
import trimesh
import numpy as np

shape = input("Enter the 3D shape you want to draw (cube or sphere): ")

if shape == "cube":
    side_length = float(input("Enter the side length of the cube: "))
    cube_mesh = trimesh.creation.box(side_length=side_length)
    scene = pyrender.Scene(ambient_light=[0.5, 0.5, 0.5])
    camera_pose = np.eye(4)
    camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.0)
    scene.add(cube_mesh, pose=np.eye(4))
    scene.add(camera, pose=camera_pose)
    r = pyrender.OffscreenRenderer(viewport_width=640, viewport_height=480)
    color, depth = r.render(scene)
    pyrender.Viewer(scene, use_raymond_lighting=True)

elif shape == "sphere":
    radius = float(input("Enter the radius of the sphere: "))
    sphere_mesh = trimesh.creation.icosphere(radius=radius)
    scene = pyrender.Scene(ambient_light=[0.5, 0.5, 0.5])
    camera_pose = np.eye(4)
    camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.0)
    scene.add(sphere_mesh, pose=np.eye(4))
    scene.add(camera, pose=camera_pose)
    r = pyrender.OffscreenRenderer(viewport_width=640, viewport_height=480)
    color, depth = r.render(scene)
    pyrender.Viewer(scene, use_raymond_lighting=True)

else:
    print("Invalid 3D shape selected. Please enter 'cube' or 'sphere'.")

