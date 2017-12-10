import utils as ut
import numpy as np
import numba
import time

import hashlib


def expand(cell, mapper, depths, depth):
    neighbors = mapper[cell]

    if neighbors is None:
        return depth

    result = []

    for nei in neighbors:
        if nei in depths:
            result += [(depths[nei] + 1)]
        else:
            result += [expand(nei, mapper, depths, depth=depth+1)]

    return max(result)

if __name__ == '__main__':
    lines = ut.read_text("inputs/day7.txt")
    mapper = {}
    for l in lines:
        l = l.replace("\n","")
        ll = l.split("->")
        name = ll[0]
        name = name.split(" ")[0].strip()
        if len(ll) == 1:
            mapper[name] = None
        else:
            vals = ll[1]

            
            mapper[name] = [v.strip() for v in vals.split(",")]

    depths = {}
    for k in mapper:
        depths[k] = expand(k, mapper, depths, 0)
        print(depths)

    aaa = np.array(list(depths.values()))
    i = np.argmax(aaa)
    print(list(depths.keys())[i])
    import ipdb; ipdb.set_trace()  # breakpoint 27d9dd43 //

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


    
    