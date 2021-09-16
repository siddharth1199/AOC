import re
import sys

UNIQUE_MOLS = set()

def load_file(path):
    with open(path, "r") as f:
        part1 = f.readlines()
        org_mol = part1[-1]
    return part1, org_mol

def fission_fusion(match, replace, org_mol):
    match_iter = re.finditer(match, org_mol)
    for m in match_iter:
        new_mol = org_mol[:m.span()[0]] + replace + org_mol[m.span()[1]:]
        UNIQUE_MOLS.add(new_mol)
    
def main(path):
    lines, org_mol = load_file(path)
    for line in lines[:-2]:
        match, _, replace = line.split()
        fission_fusion(match, replace, org_mol)
    print('Part 1 = ',len(UNIQUE_MOLS))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python [script.py] [input.txt]")
    else:
        main(sys.argv[1]) 
    