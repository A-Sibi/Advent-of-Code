from typing import List

s1 = [3,5,2,5,4,3,2,2,3,5,2,3,2,2,2,2,3,5,3,5,5,2,2,3,4,2,3,5,5,3,3,5,2,4,5,4,3,5,3,2,5,4,1,1,1,5,1,4,1,4,3,5,2,3,2,2,2,5,2,1,2,2,2,2,3,4,5,2,5,4,1,3,1,5,5,5,3,5,3,1,5,4,2,5,3,3,5,5,5,3,2,2,1,1,3,2,1,2,2,4,3,4,1,3,4,1,2,2,4,1,3,1,4,3,3,1,2,3,1,3,4,1,1,2,5,1,2,1,2,4,1,3,2,1,1,2,4,3,5,1,3,2,1,3,2,3,4,5,5,4,1,3,4,1,2,3,5,2,3,5,2,1,1,5,5,4,4,4,5,3,3,2,5,4,4,1,5,1,5,5,5,2,2,1,2,4,5,1,2,1,4,5,4,2,4,3,2,5,2,2,1,4,3,5,4,2,1,1,5,1,4,5,1,2,5,5,1,4,1,1,4,5,2,5,3,1,4,5,2,1,3,1,3,3,5,5,1,4,1,3,2,2,3,5,4,3,2,5,1,1,1,2,2,5,3,4,2,1,3,2,5,3,2,2,3,5,2,1,4,5,4,4,5,5,3,3,5,4,5,5,4,3,5,3,5,3,1,3,2,2,1,4,4,5,2,2,4,2,1,4]
s_example = [3,4,3,1,2]

def part1_NaiveAlgorithm(s : List, days : int) -> int:
    for x in range(days):
        counter = 0
        for i in range(len(s)):
            if s[i] == 0:
                counter += 1
        for i in range(len(s)):
            s[i] = s[i] - 1
            if s[i] == -1:
                s[i] = 6
        for _ in range(counter):
            s.append(8)
        # print(x) # optional counter
    return len(s)

def part2_GenCounter(s : list, days : int) -> int:
    genCounter = [0] * 9
    for el in s:
        genCounter[el] += 1

    for _ in range(days):
        newGens = genCounter[0] # number of fish currently on cycle 0
        genCounter = genCounter[1:]
        genCounter.append(0)
        genCounter[6] += newGens
        genCounter[8] += newGens
    return sum(gen for gen in genCounter)


print(part2_GenCounter(s1, 256))