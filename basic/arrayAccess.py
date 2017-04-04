

array = [[1],[2],[3],[4]]

def aaMaxVal(aa):
    val = max(aa[0])
    for a in aa:
        val = max(val, max(a))
    return val

print aaMaxVal(array)
