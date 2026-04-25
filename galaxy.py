import pyvista as pv
import numpy as np

n = 3000
theta = np.random.rand(n) * 4 * np.pi

# Spread stars out more with larger radius scaling
r = theta * 3.0 + np.random.normal(0, 3, n)  # Add some randomness to break up the spiral
x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.random.normal(0, 4, n)  # Larger vertical scatter for a disk

points = np.column_stack((x, y, z))

cloud = pv.PolyData(points)

plotter = pv.Plotter()
plotter.set_background('black')  # type: ignore
plotter.add_mesh(cloud, color='white', point_size=5)
plotter.add_mesh(pv.Sphere(radius = 0.3), color = "yellow")
plotter.show()
