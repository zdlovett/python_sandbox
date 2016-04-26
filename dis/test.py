import dis
import numpy as np

def _filter_pixel(self, row):
    slope = 20 #max delta in mm - this should become a scale factor based on FOV
    output = []
    for i in range(1, len(row)-2):
        center = int(row[i])
        right = int(row[i-1])
        left = int(row[i+1])

        if abs(center - right) < slope or abs(center - left) < slope:
            output.append(row[i])
        elif abs(left - right) < slope*2 or abs(right - left) < slope*2:
            ave = (row[i+1] + row[i-1]) / self.u16ops[2]
            output.append(ave)
        else:
            output.append(self.u16ops[0])

    return output

print "filter"
dis.dis(_filter_pixel)
