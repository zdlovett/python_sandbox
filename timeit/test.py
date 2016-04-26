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
        elif abs(left - right) < slope2:
            buf_filter_row[i] = (row[i+1] + row[i-1]) /u16ops[2]
        else:
            buf_filter_row[i] = u16ops[0]
    return buf_filter_row[0:len(row)]


output = filter_image(image)
print np.shape(output), output.dtype

result = timeit.timeit(stmt=test_filter, timer=time.clock, number=50)
print "CPU time per filter loop:", result / 50.0, "over 50 loops"
