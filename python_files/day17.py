import sys

def parse_inputs(path):
    containers = []
    for line in open(path):
        container = line.strip()
        containers.append(int(container))
    return containers


def containers_combination(quantity, container_sizes):
    combos = 0
    for i in range(len(container_sizes)):
        container_size = container_sizes[i]
        if container_size == quantity:
            combos += 1
        elif container_size < quantity:
            remaining_quant = quantity - container_size
            combos += containers_combination(remaining_quant, container_sizes[i+1:])
    return combos


def main(path):
    containers = parse_inputs(path)
    containers.sort(reverse=True) #Start from largest container
    print('Number of combinations =', containers_combination(150, containers))

    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python [script.py] [input.txt]')
    else:
        main(sys.argv[1]) 