import utils as ut
import numpy as np



if __name__ == '__main__':
    lines = ut.read_string("inputs/day5_1.txt")

    digits = list(map(int, lines.replace("\n"," ").split()))

    n = len(digits)

    i = 0
    steps = 0
    while True:
        tmp = i

        i += digits[i]

        digits[tmp] += 1 

        steps += 1

        if i >= n:
            break

    print("steps: %d" % steps)


    
    