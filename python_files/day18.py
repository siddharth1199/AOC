import sys
import itertools
def read_file(path):
    with open(path) as f:
        lines = [x.strip() for x in f.readlines()]
        grid = {}
        for y in range(100):
            for x in range(100):
                grid[x, y] = 0 if lines[y][x] == '.' else 1
        return grid
        f.close()


def part_1(grid):
    updated_grid = {}
    for x in range(100):
        for y in range(100):
            val = grid.get((x-1, y-1), 0) + grid.get((x-1, y), 0) + grid.get((x-1, y+1), 0) + grid.get((x, y-1), 0) \
                 + grid.get((x, y+1), 0) + grid.get((x+1, y-1), 0) + grid.get((x+1, y), 0) + grid.get((x+1, y+1), 0)
            if grid[x, y]:
                updated_grid[x, y] = 1 if val in [2, 3] else 0
            else:
                updated_grid[x, y] = 1 if val == 3 else 0
    return updated_grid

def main(path):
    # Part one
    grid = read_file(path)
    for _ in itertools.repeat(None, 100):
        grid = part_1(grid)
    print('Part 1 =', sum(grid.values()))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python [script.py] [input.txt]')
    else:
        main(sys.argv[1]) 