import math


"""intersil params"""
"""
x = 6 #FOVX in degrees
y = 6 #FOVY in degrees
p = 90.0 #Emitter power in mW
d = 0.2 #distance from emitter in mm
D = None #duty cycle, 0 - 1
n = 8 #number of emittors
"""

"""ESPROS params"""
x = 90 #FOVX in degrees
y = 90 #FOVY in degrees
p = 1030.0 #Emitter power in mW
d = 0.2 #distance from emitter in mm
D = None #duty cycle, 0 - 1
n = 8 #number of emittors


"""ESPROS params for high power board"""
"""
x = 90 #FOVX in degrees
y = 90 #FOVY in degrees
p = 2000.0 #Emitter power in mW
d = 0.2#distance from emitter in m
D = None #duty cycle, 0 - 1
n = 32 #number of emittors
"""


def deg_to_rad(d):
    return d * 2 * math.pi / 360.0

"""given the FOVX FOVY and distance calculate the plane area assuming square projection"""
def area(x, y, d):
    x = deg_to_rad(x)
    y = deg_to_rad(y)
    x_edge = 2 * d * math.tan(x/2)
    y_edge = 2 * d * math.tan(y/2)

    area = x_edge * y_edge #area in m^2 at a given distance
    return area

"""take power in mW and area in m^2 and output W / m^2"""
def power_per_meter(p_total, area):
    return (p_total / 1000) / area #units in W / m^2

print "far field area:", area(x,y,d)
output = power_per_meter( p, area(x,y,d)) * n
print "Total power at ", d , "mm from device is", output, "W / m^2"
