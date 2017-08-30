import numpy as np
import matplotlib.pyplot as plt
from data import startingData, ifg_sphere

timespace = np.fromiter(ifg_sphere, dtype=float)
shift = len(timespace) // 2
freqspace = np.fft.fft(timespace, 2*len(timespace))
freqspace = abs(freqspace[0:len(timespace)])

#zero out the first part of the range
for i in range(25):
    freqspace[i] = 0

print(len(freqspace))

plt.plot(freqspace)
plt.plot(timespace)

plt.show()
