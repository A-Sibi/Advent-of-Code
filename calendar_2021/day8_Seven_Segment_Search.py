from typing import Counter


def read(file_name : str) -> list:
    with open(f'data/{file_name}.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip().split() for line in lines]
    return lines

def part1(lines : list) -> int:
    approvedLenValues = [2,3,4,7]
    counter = 0
    for line in lines:
        for i in range(-1,-5,-1):
            if len(line[i]) in approvedLenValues:
                counter += 1
    return counter

def decodeline(line : list) -> int:
    decodedNums = {}
    decodedValues = {}
    # line = line[0].split()
    codedNums = line[:10]
    for el in codedNums:
        if len(el) == 2:
            decodedNums[el] = 1
            decodedValues[1] = el
        elif len(el) == 4:
            decodedNums[el] = 4
            decodedValues[4] = el
        elif len(el) == 3:
            decodedNums[el] = 7
            decodedValues[7] = el
        elif len(el) == 7:
            decodedNums[el] = 8
            decodedValues[8] = el

    occur = 0
    for el in codedNums:
        if decodedValues[1][0] in el:
            occur += 1
    if occur == 9:
        x2 = decodedValues[1][0]
        x1 = decodedValues[1][1]
    else:
        x1 = decodedValues[1][0]
        x2 = decodedValues[1][1]

    for el in codedNums: # finding number 3
        if len(el) == 5 and (x1 in el) and (x2 in el):
            decodedNums[el] = 3
            decodedValues[3] = el
            break
    for el in codedNums: # finding number 2
        if len(el) == 5 and (x1 in el) and (x2 not in el):
            decodedNums[el] = 2
            decodedValues[2] = el
            break
    for el in codedNums: # finding number 5
        if len(el) == 5 and (x1 not in el) and (x2 in el):
            decodedNums[el] = 5
            decodedValues[5] = el
            break
    nine = decodedValues[5] + x1
    
    for el in codedNums: # finding number 9
        if set(decodedValues[5] + x1) == set(el):
            decodedNums[el] = 9
            decodedValues[9] = el

    for el in codedNums: # finding number 0
        if x1 in el and el not in decodedNums.keys():
            decodedNums[el] = 0
            decodedValues[0] = el

    for el in codedNums: # finding number 6
        if el not in decodedNums.keys():
            decodedNums[el] = 6
            decodedValues[6] = el

    value = ''
    for el in line[11:]:
        for key in decodedNums.keys():
            if set(el) == set(key):
                value += str(decodedNums[key])
    

    return int(value)

line = 'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'



def decodeDoc(lines : list) -> int:
    total = 0
    for line in lines:
        total += decodeline(line)
    return total

print(decodeDoc(read('day8')))