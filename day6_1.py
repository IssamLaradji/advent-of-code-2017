import utils as ut
import numpy as np
import numba
import time

import hashlib
@numba.jit(nopython=True)
def argmax(blocks):
    max = -1
    ind = -1
    for i, b in enumerate(blocks):
        if b > max:
            ind = i 
            max = b

    return max, ind


@numba.jit(nopython=True)
def redistribute(blocks):
    max, ind = argmax(blocks)
    n = len(blocks)
    blocks[ind] = 0

    for i in range(ind+1, ind+1+max):
        j = i % n
        blocks[j] += 1 

    return blocks


if __name__ == '__main__':
    blocks = ut.read_string("inputs/day6_1.txt")
    blocks = list(map(int, blocks.replace("\n"," ").split()))
    #blocks = [0, 2, 7, 0]

    #{{hashlib.md5(b'Hello World')
        
    history = {}
    steps = 0
    while True :
        code = str(blocks)
        if code in history:
            print("steps: %d - loop: %d" % (steps, steps - history[code]))
            break
        else:
            history[code] = steps
            blocks = redistribute(blocks)
            steps += 1
    import ipdb; ipdb.set_trace()  # breakpoint 7586fbfb //

    #digits = "0 3 0 1 -3"
    
    
    s = time.time()

    t = time.time() - s

    print("steps: %d - time: %.3f" % (steps, t))


    
    