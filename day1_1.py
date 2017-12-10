import utils as ut

if __name__ == '__main__':
    lines = ut.read_text("inputs/day1_1.txt")
    digits = lines[0]
    n_digits = len(digits)

    d_sum = 0
    for i in range(n_digits):
        d = digits[i]

        if i == (n_digits - 1):
            d_next = digits[0]
        else:
            d_next = digits[i+1]

        if int(d) == int(d_next):
            d_sum += int(d)
        

    print(d_sum)



