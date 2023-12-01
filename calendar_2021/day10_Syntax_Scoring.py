from math import ceil
def read(file_name : str) -> list:
    with open(f'data/{file_name}.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def corruptedScore(lines : list) -> int:
    score = 0
    for line in lines:
        symbols = []
        for i in range(len(line)):
            if line[i] == '(' or line[i] == '[' or line[i] == '{' or line[i] == '<':
                symbols.append(line[i])

            if line[i] == ')':
                if symbols[-1] == '(':
                    symbols.pop()
                else:
                    score += 3
                    break
            
            if line[i] == ']':
                if symbols[-1] == '[':
                    symbols.pop()
                else:
                    score += 57
                    break
            if line[i] == '}':
                if symbols[-1] == '{':
                    symbols.pop()
                else:
                    score += 1197
                    break
            if line[i] == '>':
                if symbols[-1] == '<':
                    symbols.pop()
                else:
                    score += 25137
                    break
            
    return score


def isCorrupted(line : str) -> bool:
    symbols = []
    for i in range(len(line)):
        if line[i] == '(' or line[i] == '[' or line[i] == '{' or line[i] == '<':
            symbols.append(line[i])

        if line[i] == ')':
            if symbols[-1] == '(':
                symbols.pop()
            else:
                return True
        
        if line[i] == ']':
            if symbols[-1] == '[':
                symbols.pop()
            else:
                return True
        if line[i] == '}':
            if symbols[-1] == '{':
                symbols.pop()
            else:
                return True
        if line[i] == '>':
            if symbols[-1] == '<':
                symbols.pop()
            else:
                return True
        
    return False

def incompleteScore(lines : list) -> int:
    allScores = []
    for line in lines:
        if isCorrupted(line):
            continue
        score = 0
        symbols = []
        for i in range(len(line)):
            if line[i] == '(' or line[i] == '[' or line[i] == '{' or line[i] == '<':
                symbols.append(line[i])

            if line[i] == ')':
                if symbols[-1] == '(':
                    symbols.pop()
                else:
                    print('Error!')
            
            if line[i] == ']':
                if symbols[-1] == '[':
                    symbols.pop()
                else:
                    print('Error!')
            if line[i] == '}':
                if symbols[-1] == '{':
                    symbols.pop()
                else:
                    print('Error!')
            if line[i] == '>':
                if symbols[-1] == '<':
                    symbols.pop()
                else:
                    print('Error!')

        while len(symbols) > 0:
            score *= 5
            if symbols[-1] == '(':
                score += 1
                symbols.pop()
            elif symbols[-1] == '[':
                score += 2
                symbols.pop()
            elif symbols[-1] == '{':
                score += 3
                symbols.pop()
            elif symbols[-1] == '<':
                score += 4
                symbols.pop()
        allScores.append(score)
    
    allScores.sort()
    print(allScores)
    return allScores[len(allScores)//2]

lines = read('day10')
print(incompleteScore(lines))