import utils as ut
import numpy as np
import numba

@numba.jit(nopython=True)
def fast(digits):
    n = len(digits)

    i = 0
    steps = 0
    while True:
        tmp = i

        i += digits[i]
        if digits[tmp] >= 3:
            digits[tmp] -= 1
        else: 
            digits[tmp] += 1 

        steps += 1

        if i >= n or i < 0:
            break

    return steps
if __name__ == '__main__':
    digits = ut.read_string("inputs/day5_2.txt")
    #digits = "0 3 0 1 -3"
    digits = list(map(int, digits.replace("\n"," ").split()))
    import time
    s = time.time()
    steps = fast(digits)
    t = time.time() - s

    print("steps: %d - time: %.3f" % (steps, t))


    
    