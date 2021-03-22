import time
import sys

start_time = time.time()


def load_file(path):
    with open(path) as f:
        lines = [line.strip().split(" -> ") for line in f]
        return lines


def pre_process(lines):
    result = {}
    for line in lines:
        command = line[0]
        if " " in command:
            instruction = command.split(" ") # If there is a space, it means it is a command like 
            instruction = [int(x) if x.isdigit() else x for x in instruction] # Convert the digits to int
            result[line[1]] = instruction
        else:
            result[line[1]] = int(command) if command.isdigit() else command
        
    return result


def signal_value(wire_name, commands_dict):
    if isinstance(wire_name, int):
        return wire_name # If it's numeric, return the value
    else:
        bit_op = commands_dict.get(wire_name)

        if isinstance(bit_op, int):
            return bit_op # If it's numeric, return the value

        elif isinstance(bit_op, str):
            return signal_value(bit_op, commands_dict) # If it's a string, pass it back into the function
        else:              
            if bit_op[1] == "AND":
                output = signal_value(bit_op[0], commands_dict) & signal_value(bit_op[2], commands_dict)
            elif bit_op[1] == "OR":
                output = signal_value(bit_op[0], commands_dict) | signal_value(bit_op[2], commands_dict)
            elif bit_op[1] == "RSHIFT":
                output = signal_value(bit_op[0], commands_dict) >> signal_value(bit_op[2], commands_dict)
            elif bit_op[1] == "LSHIFT":
                output = signal_value(bit_op[0], commands_dict) << signal_value(bit_op[2], commands_dict)
            elif bit_op[0] == "NOT":
                output = ~signal_value(bit_op[1], commands_dict)
            else:
                print('error, operator not recognized')

        commands_dict[wire_name] = output
    return output


def main(path):
    input_file = pre_process(load_file(path))
    result_signal = signal_value("a", input_file) # Get A value 
    # Part B
    input_file = pre_process(load_file(path)) # reset signal
    input_file["b"] = result_signal # Assign value of a to b
    result_signal_b = signal_value("a", input_file) # New signal
    print('part 2', result_signal_b) 
    end_time = time.time()
    duration = end_time - start_time
    print('The code took {} milliseconds to execute'.format(1000 * duration))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])