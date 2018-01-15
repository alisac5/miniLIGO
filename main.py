import numpy as np

from injection import *

# Global flags
is_inj = False

# Some constants
lux_len = 100
dist_len = 100

# A looped array to hold lux values
lux_arr = np.zeros(lux_len)
lux_idx = 0

# A looped array to hold distance calculations based on lux
dist_arr = np.zeros(dist_len)
dist_idx = 0

while(True):
    # Read lux data
    new_lux = get_lux()
    new_lux += get_inj() # Add injection if applicable

    # Store lux data
    lux_arr[lux_idx] = new_lux
    lux_idx += 1

    # Calculate distance
    new_dist = get_dist(lux_arr, lux_idx)

    # Store distance data
    dist_arr[dist_idx] = new_dist
    dist_idx += 1

    # Plot lux data
    draw_plot(lux_arr, lux_idx)

    # Plot distance data
    draw_plot(dist_arr, dist_idx)
