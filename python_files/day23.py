import sys

INSTRUCTIONS = []

def parse_file(path):
    with open(path) as f:
        for line in f:
            line = line.strip()
            offset = 0
            if ',' in line:
                splitting = line.split(', ')  # For cases like jie r, offset
                offset = int(splitting[1])
                line = splitting[0]
            splitting = line.split(' ')
            inst = splitting[0]
            reg = splitting[1]
            INSTRUCTIONS.append((inst, reg, offset))
        f.close()

def execute_commands(reg_values):
    steps = 0
    while len(INSTRUCTIONS) > steps >= 0:
        current_command = INSTRUCTIONS[steps]
        if current_command[0] == 'hlf':
            reg_values[current_command[1]] /= 2 # Half the register value
        elif current_command[0] == 'tpl':
            reg_values[current_command[1]] *= 3 # Triple the value
        elif current_command[0] == 'inc':
            reg_values[current_command[1]] += 1 # Increse value by 1
        elif current_command[0] == 'jmp':
            steps += int(current_command[1])        # Move n commands and skip reamining
            continue             
        elif ((current_command[0] == 'jie') & (reg_values[current_command[1]] % 2 == 0)) | ((current_command[0] == 'jio') & (reg_values[current_command[1]] == 1)) :
            steps += current_command[2]         # Move n commands if condition met and skip reamining
            continue 

        steps += 1
    return reg_values

def main(path):
    part1 = {'a': 0, 'b': 0}
    part2 = {'a': 1, 'b': 0}
    parse_file(path)
    print('part 1 = ', execute_commands(part1)['b'])
    print('part 2 = ', execute_commands(part2)['b'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
        