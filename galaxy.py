import pyvista as pv
import numpy as np
n = 3000
theta = np.random.rand(n) * 4 * np.pi
r = theta * 0.2
x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.random.rand(n) * 0.2

points = np.column_stack((x, y, z))
cloud = pv.PolyData(points)
plotter = pv.Plotter()
plotter.set_background('black')  # type: ignore
plotter.add_mesh(cloud, color='white', point_size=5)
plotter.add_mesh(pv.Sphere(radius = 0.3), color = "yellow")
plotter.show()
