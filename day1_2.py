import utils as ut

if __name__ == '__main__':
    lines = ut.read_text("inputs/day1_2.txt")
    digits = lines[0]
    #digits = "123123"
    n_digits = len(digits)

    n_steps = int(n_digits / 2)

    d_sum = 0
    for i in range(n_digits):
        d = digits[i]

        if i < n_steps:
            d_next = digits[i+n_steps]
        else:
            d_next = digits[n_steps - (n_digits - i)]

        if int(d) == int(d_next):
            d_sum += int(d)
    
    print(d_sum)

