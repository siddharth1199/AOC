from collections import namedtuple
import re
import sys

regex_extractor = re.compile(r"^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)") 
Ingredient = namedtuple('Ingredient', ['capacity', 'durability', 'flavor', 'texture', 'calories']) 

def read_file(path):
    with open(path, 'r') as f:
        ingredients = {}
        for line in f:
            groups = regex_extractor.match(line)
            ingredient = Ingredient._make([int(item) for item in groups.groups()[1:]])
            ingredients[groups.group(1)] = ingredient
        return ingredients


def calculate_score(ing):
    score = max_score = 0

    for i in range(0, 100):
        for j in range(0, 100 - i):
            for k in range(0, 100 - i - j):
                l = 100 - i - j - k
                cap = ing['Candy'][0] * i + ing['Chocolate'][0] * j + ing['Sprinkles'][0] * k + ing['Sugar'][0] * l
                dur = ing['Candy'][1] * i + ing['Chocolate'][1] * j + ing['Sprinkles'][1] * k + ing['Sugar'][1] * l
                fla = ing['Candy'][2] * i + ing['Chocolate'][2] * j + ing['Sprinkles'][2] * k + ing['Sugar'][2] * l
                tex = ing['Candy'][3] * i + ing['Chocolate'][3] * j + ing['Sprinkles'][3] * k + ing['Sugar'][3] * l

                if cap <= 0 or dur <= 0 or fla <= 0 or tex <= 0:
                    score = 0
                    continue
                score = cap * dur * fla * tex
                max_score = max(max_score, score)
    return max_score


def main(path):
    ingredients = read_file(path)
    print('max score = ', calculate_score(ingredients))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1]) 