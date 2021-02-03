with open('../inputs/day3_andrew.txt', "r") as f:
    s = f.read()

final_cord = [(0, 0)]
santa = [0, 0]
robo = [0, 0]

for move in s:
    
    if move == '^':
        santa = [santa[0], santa[1]+1]
    elif move == "v":
        santa = [santa[0], santa[1]-1]
    elif move == "<":
        santa = [santa[0]-1, santa[1]]
    elif move == ">":
        santa = [santa[0]+1, santa[1]]
    final_cord.append(santa)    
    
print('Part 1 = ', len([list(x) for x in set(tuple(x) for x in final_cord)]))

final_cord = [(0, 0)]
santa = [0, 0]
robo = [0, 0]

for count, move in enumerate(s):
    if count % 2 ==0:
        if move == '^':
            santa = [santa[0], santa[1]+1]
        elif move == "v":
            santa = [santa[0], santa[1]-1]
        elif move == "<":
            santa = [santa[0]-1, santa[1]]
        elif move == ">":
            santa = [santa[0]+1, santa[1]]
        final_cord.append(santa)    
    else:
        if move == '^':
            robo = [robo[0], robo[1]+1]
        elif move == "v":
            robo = [robo[0], robo[1]-1]
        elif move == "<":
            robo = [robo[0]-1, robo[1]]
        elif move == ">":
            robo = [robo[0]+1, robo[1]]
        final_cord.append(robo)
print('Part 2 = ', len([list(x) for x in set(tuple(x) for x in final_cord)]))