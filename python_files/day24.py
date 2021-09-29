from itertools import combinations
from functools import reduce
import sys

def load_file(path):
    with open(path, "r") as f:
        part1 = [int(line.strip()) for line in f]
    return part1

def main(path, groups):
    weights = load_file(path)
    total_weight = sum(weights) / groups
    min_quant_list = []
    for i in range(1, len(weights)):
        lowest_quantum = 9999999999999
        for group in combinations(weights, i):
            if sum(group) == total_weight:
                lowest_quantum = min(reduce((lambda x, y: x * y), group), lowest_quantum)
                min_quant_list.append(lowest_quantum)
    print('Answer for {} groups is {}'.format(groups, min(min_quant_list)))
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("USAGE: python [script.py] [input.txt], [groups]")
    else:
        main(sys.argv[1], int(sys.argv[2]))
