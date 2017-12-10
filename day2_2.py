import utils as ut

if __name__ == '__main__':
    lines = ut.read_text("inputs/day2_2.txt")
    
    checksum = 0

    n_lines = len(lines)
    for line in lines:
        intList = list(map(int, line.replace("\n","").split()))
        n = len(intList)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                num = intList[i] / intList[j]

                if num == int(num):
                    checksum += num 
                    n_lines -= 1

    assert n_lines == 0
    print(int(checksum))



