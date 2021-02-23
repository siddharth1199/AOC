import sys
import re

twice_no_overlap = re.compile(r"(\w{2}).*?(\1)")
dup_pair_re = re.compile(r"(\w).\1")


def load_file(path):
    with open(path, "r") as f:
        input_file = f.read().strip()
        word_list = input_file.split("\n")
        return word_list


def is_nice2(word):
    return (twice_no_overlap.search(word) is not None) & (dup_pair_re.search(word) is not None)


def main(path):
    word_list = load_file(path)
    print("Nice strings: {}".format(sum(1 for word in word_list if is_nice2(word)))) # Taken from f, really nice way to sum True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1]) 
