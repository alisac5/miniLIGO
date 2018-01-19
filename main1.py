import seaborn as sns
sns.set_style('darkgrid')
import time
import numpy as np
import matplotlib.pyplot as plt
def calibrate(lux):
    return np.sin(np.random.rand())

i = 0
plt.figure()
plt.ion()
import tsl2591
from audiolizer import main as audiolize
lst = []
tsl = tsl2591.Tsl2591()
while True:
    full, ir = tsl.get_full_luminosity()
    lux = tsl.calculate_lux(full,ir)
    strain = calibrate(lux)

  # plot strain as y-data point
    if len(lst)>50:
        del lst[0]
    lst.append(strain)
    plt.plot(i, lst)
    i+=0.1
    plt.show()
    plt.pause(0.01)
    plt.xlim((i*4/10-10,i*4/10+10))

  # send to audio
    # audiolize(strain)

while True:
    plt.pause(0.05)
