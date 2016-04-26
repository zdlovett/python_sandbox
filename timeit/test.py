import timeit
import time
import numpy as np
import cv2

u16ops = np.asarray([0,1,2,3,4,5], np.uint16)
image = np.random.rand(240, 320)
image = np.multiply(image, 15000)
image = np.asarray(image, np.uint16)


def test_filter():
    return filter_image(image)


buf_filter_row = np.asarray([0] * max(np.shape(image)), np.uint16)

def faster_filter(image):
    image = cv2.medianBlur(image, 3) #~1ms

    slope = 20
    slope2 = slope*2
    width, height = np.shape(image)

    center = int(image[1,1])
    right = int(image[0, 1])
    left = int(image[2, 1])
    top = int(image[1,2])
    bottom = int(image[1,0])

    for x in range(1, width-2):
        for y in range(1,height-2):
            bottom = center
            center = top
            right = int(image[x-1, y])
            left = int(image[x+1, y])
            top = int(image[x,y+1])

            if abs(center - right):
                pass



def filter_image(image):
    image = cv2.medianBlur(image, 3)
    image = _filter_for_flying(image)
    return image

def _filter_for_flying(image):
    # 0 = column, 1 = row
    image = np.apply_along_axis(_filter_pixel, 1, image)
    return np.apply_along_axis(_filter_pixel, 0, image)

def _filter_pixel(row):
    slope = 20 #max delta in mm - this should become a scale factor based on FOV
    slope2 = slope * 2

    right = None
    center = int(row[0])
    left = int(row[1])

    for i in range(1, len(row)-2):
        right = center
        center = left
        left = int(row[i+1])

        if abs(center - right) < slope or abs(center - left) < slope:
            buf_filter_row[i] = row[i]
        elif abs(left - right) < slope2 or abs(right - left) < slope2:
            buf_filter_row[i] = (row[i+1] + row[i-1]) /u16ops[2]
        else:
            buf_filter_row[i] = u16ops[0]
    return buf_filter_row[0:len(row)]

def simple_alocate():
    a = []
    for i in range(10000):
        a.append(i)
    return a

buf = []
for i in range(10000):
    buf.append(0)

def pre_alocate():
    for i in range(10000):
        buf[i] = i
    return buf


def time_simple_check():
    for i in image:
        print i



def simple_check(a, b, slope):
    delta = a - b
    return delta < slope or delta > (65535 - slope)

def abs_check(a,b,slope):
    a = int(a)
    b = int(b)
    return abs(a - b) < slope


output = filter_image(image)
print np.shape(output), output.dtype

result = timeit.timeit(stmt=test_filter, timer=time.clock, number=50)
print "CPU time per filter loop:", result / 50.0, "over 50 loops"

"""
print "dynamic alocation"
print timeit.timeit(stmt=simple_alocate, timer=time.clock, number=10000)
print "static alocation"
print timeit.timeit(stmt=pre_alocate, timer=time.clock, number=10000)
"""
