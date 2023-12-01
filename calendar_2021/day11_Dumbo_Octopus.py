import numpy as np

def read(file_name : str) -> list:
    with open(f'data/{file_name}.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return np.array([[[int(x),False] for x in row] for row in lines])

def raiseAround(matrix: list, i: int, j: int) -> list: 
    """ 
    Raises the value of 8 surrounding octopuses by 1 (if possible).\n
    Returns the updated matrix.
    """
    if i > 0: #clocwise check if possible -> update
        matrix[i-1,j,0] += 1
    if i > 0 and j < 9:
        matrix[i-1,j+1,0] += 1
    if j < 9:
        matrix[i,j+1,0] += 1
    if i < 9 and j < 9:
        matrix[i+1,j+1,0] += 1
    if i < 9:
        matrix[i+1,j,0] += 1
    if i < 9 and j > 0:
        matrix[i+1,j-1,0] += 1
    if j > 0:
        matrix[i,j-1,0] += 1
    if i > 0 and j > 0:
        matrix[i-1,j-1,0] += 1
    return matrix

def hasOvercharge(matrix: list) -> bool:
    """ 
    Checks if the matrix contains octopuses with value over 9,\n
    which haven't been ligthen up yet in this step.
    """
    for i in range(10):
        for j in range(10):
            if matrix[i,j,0] > 9 and matrix[i,j,1] == 0:
                return True
    return False


def ligths(matrix: list,n: int) -> int:
    counter = 0
    for _ in range(n):
        for i in range(10): # inital energy raise
            for j in range(10):
                matrix[i,j,0] += 1

        while hasOvercharge(matrix):
            for i in range(10):
                for j in range(10):
                    if matrix[i,j,0] > 9 and matrix[i,j,1] == 0:
                        matrix[i,j,1] = 1 # 'True' state of used energy
                        matrix = raiseAround(matrix,i,j)
                        counter += 1
        
        for i in range(10):
            for j in range(10):
                if matrix[i,j,0] > 9:
                    matrix[i,j,0] = 0
                    matrix[i,j,1] = 0
    
    return counter


def firstSimultaniousFlash(matrix):
    realMatrix = np.array([[matrix[i,j,0] for j in range(10)] for i in range(10)])
    step = 0
    while np.any(realMatrix):
        for i in range(10): # inital energy raise
            for j in range(10):
                matrix[i,j,0] += 1

        while hasOvercharge(matrix):
            for i in range(10):
                for j in range(10):
                    if matrix[i,j,0] > 9 and matrix[i,j,1] == 0:
                        matrix[i,j,1] = 1 # 'True' state of used energy
                        matrix = raiseAround(matrix,i,j)
        
        for i in range(10):
            for j in range(10):
                if matrix[i,j,0] > 9:
                    matrix[i,j,0] = 0
                    matrix[i,j,1] = 0

        realMatrix = np.array([[matrix[i,j,0] for j in range(10)] for i in range(10)])
        step += 1

    return step
    

matrix = read('day11')
print(firstSimultaniousFlash(matrix))