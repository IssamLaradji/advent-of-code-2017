import utils as ut
import numpy as np



if __name__ == '__main__':
    lines = ut.read_text("inputs/day4_1.txt")

    not_valids = 0
    for line in lines:
        passphrase = line.replace("\n", "").split()
        passphrase.sort()

        for i in range(len(passphrase)-1):
            if passphrase[i] == passphrase[i+1]:
                not_valids += 1
                break


    print("valids: %d" % (len(lines) - not_valids))
    