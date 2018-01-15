import sys

class Injection:
    def __init__(self, inj_len,  amp_step, freq_step):
        # Initializing the injection array
        self.inj_arr = np.zeros(inj_len)    
        amp = 1
        for idx in range(inj_len):
            amp += amp_step
            self.inj_arr[idx] = amp * np.sin(idx * freq_step)

def inject():
    return

def get_inj():
    return 0
