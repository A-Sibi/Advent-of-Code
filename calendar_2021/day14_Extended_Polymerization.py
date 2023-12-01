from collections import defaultdict

def read(file_name : str) -> list:
    with open(f'data/{file_name}.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        polymer = lines[0]
        instructions = lines[2:]
    return polymer,instructions

def changes(instructions: list) -> dict:
    rules = {}
    for x in instructions:
        y = x.split(' -> ')
        rules[y[0]] = y[1]
    return rules

# naive algorithm vvvv

def extendPolymerNaive(polymer: str, rules: dict) -> str: # kinda too slow...
    newPolymer = polymer[0]
    for i in range(len(polymer) - 1):
        key = polymer[i] + polymer[i+1]
        newPolymer += (rules[key] + polymer[i+1])
    return newPolymer

def finalPolymer(polymer: str, steps: int, rules: dict) -> str:
    for i in range(steps):
        polymer = extendPolymerNaive(polymer,rules)
        print(i) # slowness counter
    return polymer

def letterCounter(polymer):
    occs = defaultdict(int)
    for el in polymer:
        occs[el] += 1
    return  max(count for count in occs.values()) - min(count for count in occs.values())

# naive algorithm ^^^^




polymer, instructions = read('day14')
rules = changes(instructions)
polymer = finalPolymer(polymer,40,rules)
print(letterCounter(polymer))
