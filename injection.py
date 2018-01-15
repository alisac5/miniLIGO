import sys

class Injection:
    def __init__(self, inj_len,  amp_step, freq_step):
        # Initializing the injection signal array
        # This is a fixed array which holds the signal
        self.signal = np.zeros(inj_len)    
        amp = 1
        for idx in range(inj_len):
            amp += amp_step
            self.inj_arr[idx] = amp * np.sin(idx * freq_step)
        
        # Initializing the add_offset array
        # This is an array where sum[idx] is the next offset
        # to add to the array
        self.add_offset = np.zeros(inj_len)

        # Initializing the index and length
        self.idx = 0
        self.length = inj_len

    def inject():
        self.add_offset = [
                self.add_offset[(self.idx + i) % self.length] + self.signal[i]
                for i in range(self.length)
                ]
        return

    def get_offset():
        tmp = self.add_offset[idx]
        self.add_offset[idx] = 0
        idx += 1
        if (idx == self.length):
            idx = 0
        return tmp
