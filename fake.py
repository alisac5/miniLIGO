import seaborn as sns
sns.set_style('darkgrid')
import time
import numpy as np
import matplotlib.pyplot as plt


i = 0
plt.figure()
plt.ion()
#from audiolizer import main as audiolize
lst = []
lstx = []
while True:
    lux = np.random.rand()
    strain = np.sin(lux)
  # plot strain as y-data point
    if len(lst)>50:
        del lst[0]
        del lstx[0]
    if i%400 == 1 :
         plt.close()
         plt.figure()
    lst.append(strain)
    lstx.append(i)
    print i%5
    plt.plot(lstx, lst)
    i+=1
    plt.show()
    plt.pause(0.01)
    plt.xlim((i-10,i+10))

  # send to audio
    # audiolize(strain)

while True:
    plt.pause(0.05)
