import sys
import re
import numpy

split_regex = re.compile(r"(.+) (\d+),(\d+) through (\d+),(\d+)")
grid = [[0 for col in range(1000)] for row in range(1000)]


def load_file(path):
    with open(path, "r") as f:
        input_file = f.read().strip()
        word_list = input_file.split("\n")
        return word_list


def split_command(word):
    return split_regex.match(word).groups()


def compute_status(command, x_start, y_start, x_end, y_end):
    for x in range(int(x_start), int(x_end) + 1):
        for y in range(int(y_start), int(y_end) + 1):
            if command == "turn on":
                grid[x][y] += 1
            elif command == "turn off":
                grid[x][y] -= 1 if grid[x][y] > 0 else 0
            else:
                grid[x][y] += 2
    return grid


def main(path):
    word_list = load_file(path)
    for word in word_list:
        command, x_start, y_start, x_end, y_end = split_command(word)
        final_grid = compute_status(command, x_start, y_start, x_end, y_end)

    print(sum(map(sum, final_grid)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1]) 
