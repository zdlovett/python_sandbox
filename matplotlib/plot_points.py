"""
A simple example of an animated plot... In 3D!
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import mpl_toolkits.mplot3d.art3d as a3
import matplotlib.animation as animation

class target_point:
    def __init__(self):
        self.distance = 0
        self.speed = 0
        self.angle_az = 0
        self.angle_el = 0
        self.signal_power = 0

    def set_to_random(self):
        self.distance = np.random.rand(1)*24
        self.speed = np.random.rand(1)*10
        self.angle_az = np.random.rand(1)
        self.angle_el = np.random.rand(1)
        self.signal_power = np.random.randint(0,255,1)

    """this converts from the spherical coordinates of the module to cartesian"""
    def get_xyz(self):
        z = self.distance * math.sin(self.angle_el) * math.cos(self.angle_az)
        y = self.distance * math.sin(self.angle_el) * math.sin(self.angle_az)
        x = self.distance * math.cos(self.angle_el)
        return (x, y ,z)


def gen_target_points():
    numpoints = np.random.randint(0,64,1)
    xc = []
    yc = []
    zc = []
    for i in range(10):
        p = target_point()
        p.set_to_random()
        x, y, z = p.get_xyz()
        xc.append(x)
        yc.append(y)
        zc.append(z)

    return (xc,yc,zc)

def update_target_points(num):
    collection.remove()
    p = gen_target_points()
    collection = ax.scatter(p[0], p[1], p[2])


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)


p = gen_target_points()
collection = ax.scatter(p[0], p[1], p[2])

# Setting the axes properties
ax.set_xlim3d([0, 10.0])
ax.set_xlabel('X')

ax.set_ylim3d([0, 10.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 10.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_target_points, 1, fargs=(),
                              interval=50, blit=False)

plt.show()
