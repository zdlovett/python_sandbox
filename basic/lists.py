

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


list_o_lists = [[1,2],[2,3],[3,4],[4,5]]
for [k, l] in list_o_lists:
    if l == 4:
        k
    else:
        print "not found

if [1,2] in list_o_lists:
    print "found the complete"
else:
    print "still didn't find the complete"


#show that default params are shared between 
def foo(a_num=0, a_list=[]):
    a_list.append(a_num)
    return a_list

l = []
l = foo(1, l)
l = foo(2, l)
print(l)

foo(3)
foo(4)
l2 = foo(5)
print(l2)
