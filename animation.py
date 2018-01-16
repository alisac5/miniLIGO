import math
from injection import *
from matplotlib import pyplot as plt
from matplotlib import animation

""" use a different matplotlib layout """
plt.xkcd()

""" animation constants """
# milliseconds per second
MILLISECONDS_PER_SECOND = 1000
# frequency of animation updates (updates per second)
ANIM_FREQ = 5

""" sample background sine wave constants """
# frequency (waves per 2*pi seconds)
SAMPLE_FREQ = 1 
# amplitude
SAMPLE_AMP = 5

# create new injection
injection = Injection(100, 0.05, 0.1)

"""
Data Generator class. Initialize with a base value, and then repeatedly update the values
that are generated.
"""
class DataGenerator(object):
    def __init__(self):
        self.x = 0

    def __call__(self):
        delta_x = (1.0 / ANIM_FREQ)
        self.x += delta_x 
#        if ((self.x >= 13900.9 and self.x <= 14000.1) or (self.x >= 17900.9 and self.x <= 18000.1)):   # sample injections
#            injection.inject()
        # add "real data" (represented as a smooth sine function here) with injected data
        return self.x, SAMPLE_AMP * math.sin(SAMPLE_FREQ * self.x) + injection.get_offset()   

# create new DataGenerator
data_gen = DataGenerator()

# this function repeatedly reads the next available data point to plot
def frames():
    while True:
        yield data_gen()

# create a figure to plot on and two arrays to store the axis values
fig = plt.figure()
x = []
y = []

# this function gets called every interval milliseconds to update the plot
def animate(args):
    x.append(args[0])
    y.append(args[1])
    if len(x) > 100:   # remove old data points so plot "scrolls" along
        fig.clf()
        x.pop(0)
        y.pop(0)
    return plt.plot(x, y, color='b')

# start the visualization
anim = animation.FuncAnimation(fig, animate, frames=frames, interval=((1.0 / ANIM_FREQ) * MILLISECONDS_PER_SECOND))
plt.show()
