




#Return x*x where x=0->y
def generatorA(y):
    for i in range(y):
        yield i*i


for a in generatorA(10):
    print(a)


def foreverGenerator(array_len):
    a = [0]*array_len
    i = 0
    while True:
        a[i] += 1
        i += 1
        if i == array_len:
            i = 0
        yield a

a = foreverGenerator(10)
loops = 100
while loops > 0:
    print(a.__next__())
    loops -= 1
