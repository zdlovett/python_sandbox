
num_samples = 5
list_size = 100

l = []
for a in range(list_size):
    l.append(a)

u_dis = []
for a in range(num_samples):
    u_dis.append(l[ (list_size / num_samples) * a ])
print u_dis



def fib(n):
    s = 1
    sm1 = 0
    sm2 = None
    while n > 0:
        n -= 1
        if sm2 == None:
            print 0
        else:
            s = sm1 + sm2
            print s
        sm2 = sm1
        sm1 = s

fib(10)
