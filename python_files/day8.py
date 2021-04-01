# SAY NO TO REGEX!!!

import sys

def load_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
        return [i.strip() for i in lines]


def main(path):
    str_len = raw_len = encoded_len = 0
    lines = load_file(path)
    for l in lines:
        # Part 1
        # Eval parses the escape characters
        str_len += len(eval(l))
        raw_len += len(l)
        # Part 2
        # Basically, count each time a \ (rep by \\) and " appears and add it to the complete length
        # This is done because encoding any of the 2 chars results in 1 extra char,
        # no matter what, we just need length and not if it is \(+1\) or (+1\)"
        # Also add 2 to acount for the 2 " in the beginning and end
        encoded_len += 2 + l.count('\\') + l.count('"') + len(l)
    print('Part 1 = ', (raw_len - str_len))
    print('Part 2 = ', (encoded_len - raw_len))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
