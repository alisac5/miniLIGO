import seaborn as sns
sns.set_style('darkgrid')
import time
import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO

def calibrate(lux, full_wavelength):
    return full_wavelength*10**-9*530 + np.random.randn()*lux*10**-9*100
def inject():
    x = np.linspace(0,2,21)
    y = np.sin(x**2)*x*10**-8
    return x,y
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i = 0
plt.figure()
plt.ion()
import tsl2591
#from audiolizer import main as audiolize
lst = []
lstx = []
luxes = []
full_wavelength = 0
tsl = tsl2591.Tsl2591()
while True:
    # check for trigger
    input_state = GPIO.input(18)
    if input_state == False:
        plt.figure()
        x,y = inject()
        lsti = []
        lstj = []
        for i,j in zip(x,y):
            lsti.append(i)
            lstj.append(j)
            plt.plot(lsti,lstj)
            time.sleep(0.1)
    full, ir = tsl.get_full_luminosity()
    lux = tsl.calculate_lux(full, ir)
    strain = calibrate(lux,full_wavelength)

  # plot strain as y-data point
    if len(lst)>50:
        del lstx[0] 
        del lst[0]
    lst.append(strain)
    lstx.append(i)
    plt.plot(lstx, lst)
    i+=1
    plt.show()
    plt.pause(0.01)
    plt.xlim((i-10,i+10))

  # send to audio
  #  audiolize(strain/100)

while True:
    plt.pause(0.05)
