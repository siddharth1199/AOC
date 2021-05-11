import re
import sys
import json
 
def load_file(path):
    with open(path, "r") as f:
        part1 = f.readlines()       
    return part1

def load_json(path):
    with open(path, "r") as f:
        part_2 = json.load(f)
    return part_2

def part_1(string):
    return sum([int(n) for n in re.findall("\-?\d+", string)])


# wanted to use lru_cache if the problem scales, but lists and dicts are unhashable
def part_2(item):
    
    if isinstance(item, str):
        return 0

    if isinstance(item, int):
        return item
    
    if isinstance(item, list):  # can use if type(item) is list, but isinstance seems to be faster
        return sum([part_2(i) for i in item])

    if isinstance(item, dict):
        if 'red' in item.values():
            return 0
        return sum([part_2(i) for i in item.values()])

def main(path):
    input_1 = load_file(path)
    input_2 = load_json(path)
    print('solution to part 1 = ', part_1(str(input_1)))
    print('solution to part 2 = ', part_2(input_2))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1]) 
    