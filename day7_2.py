import utils as ut
import numpy as np
import numba
import time

import hashlib


def expand(cell, mapper, weights,  total_weight):
    neighbors = mapper[cell]

    if neighbors is None:
        return 0

    result = []
    wList = [] 
    for nei in neighbors:
        wList += [weights[nei]]
        if nei in total_weight:
            result += [total_weight[nei]]
        else:
            result += [expand(nei, mapper, weights, total_weight)]
    wList = np.array(wList)
    result = np.array(result)
    zz = wList + result

    if np.unique(zz).size != 1:
        print(zz)
        wList[0] +=  (zz[1] - zz[0])
        import ipdb; ipdb.set_trace()  # breakpoint 9a43cfb3 //

    return sum(zz)

if __name__ == '__main__':
    lines = ut.read_text("inputs/day7.txt")
    mapper = {}
    weights = {}
    for l in lines:
        l = l.replace("\n","")
        ll = l.split("->")
        name = ll[0]
        name, weight = name.split(" ")[:2]
        name = name.strip()
        weight = int(weight.strip()[1:-1])
        weights[name] = weight
        if len(ll) == 1:
            mapper[name] = None
        else:
            vals = ll[1]

            
            mapper[name] = [v.strip() for v in vals.split(",")]
            


    total_weights = {}

    for k in mapper:
        total_weights[k] = expand(k, mapper, weights,  total_weights)
        #print(total_weights)
    import ipdb; ipdb.set_trace()  # breakpoint 67de4696 //


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


    
    