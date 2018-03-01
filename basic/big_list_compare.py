import numpy as np
from multiprocessing.pool import Pool
from tqdm import tqdm
import time

print("generating large lists")
big1 = [i for i in tqdm(range(5000000))]
big2 = [i for i in tqdm(range(1000000, 6000000))]

"""
#search type one, brute force runs about 300 interations / second
print("Staring search...")
only_in_one = []
for i in tqdm(big1):
    if i in big2:
        big2.remove(i)
    else:
        only_in_one.append(i)

print(f"Only in 1:{len(only_in_one)}, only in 2:{len(big2)}")
"""
"""
#search type two, using index maps
#this will work well for sets with few repeated values
def build_map(big_list):
    index_map = {}
    for i, n in tqdm(enumerate(big_list), total=len(big_list)):
        try:
            index_map[str(n)].append(i)
        except KeyError:
            index_map[str(n)] = [i]
    return index_map

print("Building maps of item locations...")
s = time.monotonic()
map1 = build_map(big1)
map2 = build_map(big2)
e = time.monotonic() - s
print(f"Building maps took {e} seconds.")

def check(item):
    nia = []
    nib = []
    try:
        map1[item]
    except KeyError:
        nia.append(item)
    try:
        map2[item]
    except KeyError:
        nib.append(item)
    return (nia, nib)

print("Checking for the deltas now...")
s = time.monotonic()

not_in_a = []
not_in_b = []
bigbig = big1 + big2

for i in tqdm(bigbig):
    a, b = check(i)
    not_in_a.extend(a)
    not_in_b.extend(b)

e = time.monotonic() - s
print(f"finding deltas took {e} seconds")
print(len(not_in_a), len(not_in_b))
"""

#now using sets
print("converting to sets")
s = time.monotonic()
s1 = set(big1)
s2 = set(big2)

e = time.monotonic() - s
print("building sets took {e} seconds")

print("finding deltas...")
s = time.monotonic()
d = s1.difference(s2)
e = time.monotonic() - s

print(f"{len(d)} deltas found in {e} seconds")
