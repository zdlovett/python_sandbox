import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np
import math
import time
import Queue

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
        self.angle_az = np.random.rand(1) - 0.5
        self.angle_el = np.random.rand(1) - 0.5
        self.signal_power = np.random.randint(0,255,1)

    """this converts from the spherical coordinates of the module to cartesian"""
    def get_xyz(self):
        z = self.distance * math.sin(self.angle_el) * math.cos(self.angle_az)
        y = self.distance * math.sin(self.angle_el) * math.sin(self.angle_az)
        x = self.distance * math.cos(self.angle_el)
        return (x, y ,z)


class point_plotter:
    def __init__(self, point_queue):
        self.point_queue = point_queue
        self.fig = plt.figure()
        self.ax = p3.Axes3D(self.fig)

        self.ax.set_xlim3d([0, 10.0])
        self.ax.set_xlabel('X')

        self.ax.set_ylim3d([0, 10.0])
        self.ax.set_ylabel('Y')

        self.ax.set_zlim3d([0.0, 10.0])
        self.ax.set_zlabel('Z')

        self.scatter = plt.scatter([0], [0], zs=[0])
        #self.ani = animation.FuncAnimation(self.fig, self.update)
        self.plt = plt
        self.plt.ion()

    def update(self):
        print "in the update function"
        if not self.point_queue.empty():
            points = self.point_queue.get()
            print points
            self.scatter.remove()
            self.scatter = plt.scatter(points[0], points[1], zs=points[2])
            self.plt.draw()

if __name__=="__main__":

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

    point_queue = Queue.Queue()
    print "does anything happen after the plot starts?"
    plot = point_plotter(point_queue)

    while 1:
        time.sleep(1)
        print "adding point to queue"
        plot.update()
        point_queue.put(gen_target_points())
