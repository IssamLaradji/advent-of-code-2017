import utils as ut
import numpy as np
from itertools import cycle

def next_index():
    pass

def branch(digit):
    count = 1
    for i in range(1, 300):
        s = count + 1
        e = count + ((2*(i-1) + 3)*4 - 4)

        count = e

        if digit <= count:
           return {"steps": i, "digit":digit, "s": s, "e":e, "d":2*i+1}

def matrix(nrows=11, ncols = 11, max_runs=5, digit=347991):

    M = np.zeros((nrows, ncols))

    yc, xc = int(nrows/2), int(ncols/2)
    M[yc, xc] = 1
    M[yc, xc+1] = 1

    modes = cycle(["up", "left", "down", "right"])

    y, x = yc, xc+1
    mode = next(modes)         
    ind = 2
    for i in range(2, max_runs):
        if mode == "up":
            n_cells = branch(ind)["d"] - 2
        elif mode == "right":
            n_cells = branch(ind)["d"]
        else:
            n_cells = branch(ind)["d"] - 1
  
        for j in range(n_cells):
            ind += 1
            if mode == "up":
                y -= 1

            if mode == "left":
                x -= 1

            if mode == "down":
                y += 1

            if mode == "right":
                x += 1


            M[y, x] += M[y-1, x-1] + M[y-1, x] + M[y-1, x+1]
            M[y, x] += M[y, x-1] + M[y, x+1]
            M[y, x] += M[y+1, x-1] + M[y+1, x] + M[y+1, x+1]

            if M[y,x] > digit:
                print("\nFirst digit larger than %d: %d" %(digit, M[y,x]))
                return
        
        print(M[y,x])

        mode = next(modes)         

if __name__ == '__main__':
    data = 347991
    matrix(nrows=50, ncols = 50, max_runs=51, digit=data)
