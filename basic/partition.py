

def color_generator(num):
        colors = []
        for i in range(0,num):
            r = (1.0/num)*(i/float(num))
            g = (1.0/num)*((num-i)/float(num))
            b = (1.0/num)*(i/float(num))
            a = 1
            colors.append((r,g,b,a))
        return colors

for c in color_generator(10):
    print c
