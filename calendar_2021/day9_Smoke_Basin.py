import numpy as np
from collections import defaultdict

def read(file_name : str) -> list:
    with open(f'data/{file_name}.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return np.array([[int(x) for x in row] for row in lines])

def isLocalMinimum(matrix : list,row : int,col : int) -> bool:
    if row > 0:
        if matrix[row,col] >= matrix[row-1,col]:
            return False

    if row < matrix.shape[0] - 1:
        if matrix[row,col] >= matrix[row+1,col]:
            return False

    if col > 0:
        if matrix[row,col] >= matrix[row,col-1]:
            return False

    if col < matrix.shape[1] - 1:
        if matrix[row,col] >= matrix[row,col+1]:
            return False

    return True

def allLocalMinRisks(matrix):
    risk = 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            if isLocalMinimum(matrix, row, col):
                risk += matrix[row, col] + 1
    return risk


def endPoint(x : int, y : int) -> tuple:
    """
    Finds the local minumum to wich it falls.
    """
    x1 = x
    y1 = y
    while not isLocalMinimum(matrix,x1,y1):
        if matrix[x,y] == 9:
            return None
        min = matrix[x1,y1]
        minPos = (x1,y1)

        if x1 > 0:
            if matrix[x1-1,y1] < min:
                min = matrix[x1-1,y1]
                minPos = (x1-1,y1)

        if x1 < matrix.shape[0] - 1:
            if matrix[x1+1,y1] < min:
                min = matrix[x1+1,y1]
                minPos = (x1+1,y1)

        if y1 > 0:
            if matrix[x1,y1-1] < min:
                min = matrix[x1,y1-1]
                minPos = (x1,y1-1)

        if y1 < matrix.shape[1] - 1:
            if matrix[x1,y1+1] < min:
                min = matrix[x1,y1+1]
                minPos = (x1,y1+1)
        x1 = minPos[0]
        y1 = minPos[1]
    return (x1,y1)

def allBasins(matrix) -> dict:
    allBasins = defaultdict(list)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j] == 9:
                continue
            allBasins[endPoint(i,j)].append((i,j))
    return allBasins


def basinSizes(matrix):
    sizes = []
    for _, values in allBasins(matrix).items():
        sizes.append(len(values))
    sizes.sort(reverse=True)
    p = 1
    for i in range(3):
        p = p * sizes[i]
    return p

matrix = read('day9')
print(basinSizes(matrix))