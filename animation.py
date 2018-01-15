import random
import time
import math

from matplotlib import pyplot as plt
from matplotlib import animation


class RegrMagic(object):
    """Mock for function Regr_magic()
    """
    def __init__(self):
        self.x = 0

    def __call__(self):
        self.x += 0.1
        return self.x, math.sin(self.x)

regr_magic = RegrMagic()

def frames():
    while True:
        yield regr_magic()

fig = plt.figure()

x = []
y = []

def animate(args):
    x.append(args[0])
    y.append(args[1])
    if len(x) > 100:
        fig.clf()
        x.pop(0)
        y.pop(0)
    return plt.plot(x, y, color='g')

anim = animation.FuncAnimation(fig, animate, frames=frames, interval=100)
plt.show()
