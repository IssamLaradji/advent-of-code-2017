import utils as ut
import numpy as np





def branch(digit):
    count = 1
    for i in range(1, 300):
        s = count + 1
        e = count + ((2*(i-1) + 3)*4 - 4)

        count = e

        if digit <= count:
           return {"steps": i, "digit":digit, "s": s, "e":e, "d":2*i+1}
    
def quarter(dbranch):
    digit = dbranch["digit"]
    s, e, d = dbranch["s"], dbranch["e"], dbranch["d"]
    q1 = [e] + list(range(s, s+d - 1))
    q2 = list(range(q1[-1], q1[-1]+d))
    q3 = list(range(q2[-1], q2[-1]+d))
    q4 = list(range(q3[-1], q3[-1]+d))

    for q in [q1, q2, q3, q4]:
        if digit in q:
            #print(digit)
            #print(q)
            steps2center = abs(np.where(digit == np.array(q))[0][0] - int(d/2))
            #print(steps2center)
            break

    # print(q1)
    # print(q2)
    # print(q3)
    # print(q4)

    print("\nTotal steps: %d  - left/right: %d - up/down: %d" % 
         (dbranch["steps"] + steps2center, dbranch["steps"], steps2center))


if __name__ == '__main__':
    data = 347991
    quarter(branch(data))