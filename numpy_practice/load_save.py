import numpy as np
import time

filename = "data.bin"
num_insertions = 265

s = time.monotonic()
data = np.asarray(np.ones(2048*num_insertions, dtype=np.float32) * np.bartlett(2048*num_insertions), dtype=np.float32)
e = time.monotonic() - s
print(f"Generated data in {e} seconds. {data.dtype}")

s = time.monotonic()
with open(filename, 'wb') as fd:
    data.tofile(fd)
e = time.monotonic() - s
print(f"Saving data took {e} seconds")

def load_file():
    with open(filename, 'rb') as fd:
        raw_data = fd.read()
        data = np.frombuffer(raw_data, dtype=np.float32)
    return data

def np_load_file():
    with open(filename, 'rb') as fd:
        data = np.fromfile(fd, dtype=np.float32)
    return data

n_data = load_file()
npdata = np_load_file()

print(f"Lengths:{npdata.size}, {len(npdata)}")

print(f"We should have {num_insertions * 2048} elements.")
print(f"{np.shape(n_data)}, {n_data.size}, {n_data.dtype}")
print(f"{np.shape(npdata)}, {npdata.size}, {npdata.dtype}")


times = []
for i in range(1000):
    s = time.monotonic()
    load_file()
    e = time.monotonic() - s
    times.append(e)

print(f"Normal file load took {sum(times)} total time for {sum(times) / len(times)} seconds per load.")

times = []
for i in range(1000):
    s = time.monotonic()
    np_load_file()
    e = time.monotonic() - s
    times.append(e)
print(f"NP file load took {sum(times)} total time for {sum(times) / len(times)} seconds per load.")
