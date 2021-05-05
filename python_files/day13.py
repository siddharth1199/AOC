'''
Money can't buy happiness,
but it can make you awfully comfortable while you're being miserable.
- Clare Boothe Luce
'''
import itertools
import sys

happiness = {}
names = set()

def load_file(path):
    global happiness, names
    with open(path, "r") as f:
        split_line = f.readlines()
        for l in split_line:
            line = l.split()
            person_a = line[0]
            direction = line[2]
            value = int(line[3])
            person_b = line[10][:-1]

            names.add(person_a)
            names.add(person_b)

            if direction == 'lose':
                happiness[person_a+person_b] = -value
            elif direction == 'gain':
                happiness[person_a+person_b] = value
            else:
                print('invalid input')
                
    return names, happiness

def find_max_happiness(names, happiness):
    max_val = 0
    for arragement in itertools.permutations(names):
        happiness_val = 0
        for person_a, person_b in zip(arragement, arragement[1:]):
            happiness_val += happiness[person_a + person_b]
            happiness_val += happiness[person_b + person_a]
            
        person_a = arragement[0]
        person_b = arragement[-1]
        happiness_val += happiness[person_a + person_b]
        happiness_val += happiness[person_b + person_a]
        
        max_val = max(max_val, happiness_val)
        
    return max_val


def main(path):
    names, happiness = load_file(path)
    print('part1 = ', find_max_happiness(names, happiness))
    # part b
    for person in names:
        happiness['me' + person] = happiness[person + 'me'] = 0
    names.add('me')
    print('part2 = ' ,find_max_happiness(names, happiness))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
