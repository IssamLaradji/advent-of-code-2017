import utils as ut
import numpy as np
import numba
import time

import hashlib

def groups(l):
    stack = []
    c =0 
    garbage = False
    ignore_next = False
    upper = 0
    total = 0
    for i in range(len(l)):
        if ignore_next:
            ignore_next = False
            continue
        if "!" == l[i]:
            ignore_next = True

        else:
            #print(l[i], garbage)


            if ">" == l[i]:
                garbage = False

            if "<" == l[i] and not garbage:
                garbage = True
            elif garbage:
                total += 1
                

            if "{" == l[i] and not garbage:
                upper += 1
            if "}" == l[i] and not garbage:
                c += (1 + upper - 1)
                upper -= 1

            ignore_next = False

    print(c, total)
    import ipdb; ipdb.set_trace()  # breakpoint cd3ac9a7 //

    


if __name__ == '__main__':
    lines = ut.read_text("inputs/day9.txt")

    groups(lines[0])
    import ipdb; ipdb.set_trace()  # breakpoint 516feb18 //

    varDict = {}
    maxx = 0
    for l in lines:
        print(l)
        name, cond = l.replace("\n","").split(" if ")

        v, op, n = name.split()
        if v not in varDict:
            varDict[v] = 0

        l,c,r = cond.strip().split()
        if l not in varDict:
            varDict[l] = 0

        if eval("varDict['%s']" % l + c + r):
            if op == "inc":
                varDict[v] += int(n)
            else:
                varDict[v] -= int(n)

        maxx = max(maxx, varDict[v])

    print(np.max(list(varDict.values())))
    print(maxx)
    import ipdb; ipdb.set_trace()  # breakpoint 74153bfc //

            


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


    
    