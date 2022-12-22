import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the sphere's radius
r = 1

# Set the sphere's center point
x0, y0, z0 = 0, 0, 0

# Set the number of points to use for the sphere
n = 20

# Generate the sphere's coordinates
u = np.linspace(0, 2 * np.pi, n)
v = np.linspace(0, np.pi, n)
x = r * np.outer(np.cos(u), np.sin(v)) + x0
y = r * np.outer(np.sin(u), np.sin(v)) + y0
z = r * np.outer(np.ones(np.size(u)), np.cos(v)) + z0

# Plot the sphere
ax.plot_surface(x, y, z, color='b')

# Show the plot
plt.show()
