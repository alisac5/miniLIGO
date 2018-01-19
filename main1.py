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
    y = np.sin(x)*x
    for i in range()

PIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i = 0
plt.figure()
plt.ion()
import tsl2591
from audiolizer import main as audiolize
lst = []
luxes = []
full_wavelength = 0
tsl = tsl2591.Tsl2591()
while True:
    # check for trigger
    input_state = GPIO.input(18)
    if input_state == False:
        inject()



    strain = calibrate(lux,full_wavelength)

  # plot strain as y-data point
    if len(lst)>50:
        del lst[0]
    lst.append(strain)
    plt.plot(i, lst)
    i+=0.1
    plt.show()
    plt.pause(0.01)
    plt.xlim((i-10,i+10))

  # send to audio
    audiolize(strain/100)

while True:
    plt.pause(0.05)
