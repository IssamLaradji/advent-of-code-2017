import utils as ut

if __name__ == '__main__':
    lines = ut.read_text("inputs/day2_1.txt")
    

    checksum = 0

    for line in lines:
        ls = list(map(int, line.replace("\n","").split()))
        checksum += max(ls) - min(ls)

        

    print(checksum)



