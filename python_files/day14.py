import re
import sys

def parse_input(path):
    pattern = re.compile(r'^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$')
    names = set()
    speeds = {}
    times = {}
    rests = {}
    with open(path, 'r') as f:
        for line in f:
            name, speed, time, rest = pattern.match(line).groups()
            names.add(name)
            speeds[name] = int(speed)
            times[name] = int(time)
            rests[name] = int(rest)
    return names, speeds, times, rests

def compute_dist(speed, time, rest, total_time):
    
    comp_cycle, remainder = divmod(total_time, time + rest) # complete cycles done by the reindeer
    distance = (comp_cycle*time + min(remainder, time)) * speed # multiply speed with either the remaining time or the time the reindeer can travel (whichever is lesser) 
    return distance

def main(path):
    names, speeds, times, rests = parse_input(path)
    print('max dist = ', max([compute_dist(speeds[name], times[name], rests[name], 2503) for name in names]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1]) 
    