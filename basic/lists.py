

def change_values(a):
    print a
    i = 0
    l = len(a)
    while i < l:
        a[i] = a[i]*2
        i += 1
    print a


def values_unchanged(a):
    print a
    for i in a:
        i = i*2
    print a

def mult2(a):
    return a * 2

def inplace_map(l, f):
    for i, v in enumerate(l):
        l[i] = f(v)

a = [1,2,3,4,5,6,7,8]
b = [1,2,3,4,5,6,7,8]
print "change the values"
change_values(a)
print "the values are unchanged"
values_unchanged(b)


print "inplace map test"
inplace_map(b, mult2)
print b
