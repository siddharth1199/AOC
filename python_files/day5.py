import sys
import time
start_time = time.time() 

def load_file(path):
    return open(path)

def twice_in_row(line):
    i=0
    for j in range(0, len(line)-1):
        if line[j]==line[j+1]:
            i=0
            break
        else:
            i=1
    return i

def vowel_count(line):
    i=0
    vowels_count = (line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u'))
    if vowels_count < 3:
        i=i+1
    return i

def not_contain_string(line):
    i=0
    for s in ['ab', 'cd', 'pq', 'xy']:
        if s in line:
            i=i+1
    return i

def main(path):
    f = load_file(path)
    nice_strings = 0
    for line in f:
        if twice_in_row(line) == vowel_count(line) == not_contain_string(line) == 0:
             nice_strings = nice_strings+1
    print('Number of nice strings = {}'.format(nice_strings))
    end_time = time.time()
    duration = end_time - start_time
    print('The code took {} milliseconds to execute'.format(1000*duration))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1]) 