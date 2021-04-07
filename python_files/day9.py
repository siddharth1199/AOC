import itertools
from itertools import permutations
import re
import sys

def load_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
        return [i.strip() for i in lines]

def parse_file(file):
    path = {}
    cities = set()

    for line in file:

        line_re = re.compile(r"(\w+) to (\w+) = (\d+)")
        city_a, city_b, distance = line_re.match(line).groups()

        path[city_a + city_b] = path[city_b + city_a] = int(distance)

        cities.add(city_a)
        cities.add(city_b)
    
    return path, cities
    
    
def main(path):
    shortest = 999
    longest = 0
    raw_file = load_file(path)
    path, cities = parse_file(raw_file)
    
    for route in itertools.permutations(cities):
        route_length = 0
        
        for city_a, city_b in zip(route, route[1:]):
            route_length += path[city_a + city_b]

        if route_length < shortest:
            shortest = route_length
        if route_length > longest:
            longest = route_length    
            
    print("Shortest route length:", shortest)
    print("longest route length:", longest)
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1])
