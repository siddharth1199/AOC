import numpy as np
import sys

UPPER_LIMIT = 1000000  

def main(num_presents):
    house = np.zeros(UPPER_LIMIT)
    for dobby in range(1, UPPER_LIMIT):   
        #house[dobby::dobby] += 10 * dobby
    print('Part1 = ', np.where(house>=num_presents)[0][0])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [num_presents]")
    else:
        main(int(sys.argv[1])) 