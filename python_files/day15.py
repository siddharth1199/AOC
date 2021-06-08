from collections import namedtuple
import re
import sys
from itertools import combinations_with_replacement as combinations

line_re = re.compile(r"^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")

Ingredient = namedtuple('Ingredient', ['capacity', 'durability', 'flavor', 'texture', 'calories'])

def read_file(path):
    with open(path, 'r') as f:
        ingredients = {}
        for line in f:
            groups = line_re.match(line)      
            ingredient = Ingredient._make([int(item) for item in groups.groups()[1:]])
            ingredients[groups.group(1)] = ingredient
        return ingredients
        
def get_max_score(recipe, ingredients):
        score = max(0, sum(ingredients[item].capacity for item in recipe))
        score *= max(0, sum(ingredients[item].durability for item in recipe))
        score *= max(0, sum(ingredients[item].flavor for item in recipe))
        score *= max(0, sum(ingredients[item].texture for item in recipe))
        
        return score


def main(path):     
    ingredients = read_file(path)
    teaspoons = 100
    max_score = calorie_score = 0
    for recipe in combinations(ingredients.keys(), teaspoons):
        max_score = max(max_score, get_max_score(recipe, ingredients))
        calories = sum(ingredients[item].calories for item in recipe)
        if calories == 500:
            calorie_score = max(calorie_score, get_max_score(recipe, ingredients))
    print('part 1 and part 2 = {}, {}'.format(max_score, calorie_score))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1]) 