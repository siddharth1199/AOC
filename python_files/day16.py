import re
import sys

AUNT_SUE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def parse_inputs(path):
    input_pattern = r'Sue \d*: (.*)'
    aunts = []
    for line in open(path):
        items = re.match(input_pattern, line.strip()).group(1).split(', ')
        item_dict = dict()
        for item in items:
            item_dict[item.split(': ')[0]] = int(item.split(': ')[1])
        aunts.append(item_dict)
    return aunts


def right_sue(aunts, part_2):
    for i, aunt in enumerate(aunts, start=1):
        flag = True
        for k, v in aunt.items():
            if part_2 and (k == 'cats' or k == 'trees'):
                if AUNT_SUE[k] >= v:
                    flag = False
                    break
            elif part_2 and (k == 'pomeranians' or k == 'goldfish'):
                if AUNT_SUE[k] <= v:
                    flag = False
                    break
            elif AUNT_SUE[k] != v:
                flag = False
                break
        if flag:
            return i


def main(path):
    aunts = parse_inputs(path)
    print(right_sue(aunts, False))
    print(right_sue(aunts, True))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python [script.py] [input.txt]')
    else:
        main(sys.argv[1]) 