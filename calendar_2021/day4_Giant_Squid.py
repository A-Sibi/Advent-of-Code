import numpy as np
def drawnNums(docName : str) -> int:
    with open(f'data/{docName}.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    drawnNums = [int(num) for num in lines[0].split(',')]
    return drawnNums

def makeBoards(docName : str) -> list:
    with open(f'data/{docName}.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    allBoards = []
    board = []
    i = 2
    while i < len(lines):
        if lines[i] == '':
            allBoards.append(np.array(board,dtype=int))
            board = []
            i += 1
            continue
        row = lines[i].split()
        board.append([int(num) for num in row])
        i += 1
    return allBoards[:-1]

def isWinning(board : list) -> bool:
    for i in range(board.shape[0]):
        if np.all(board[i] == -1) or np.all(board.T[i] == -1):
            return True
    return False

def score(board : list, drawnNum : int) -> int:
    sum = 0
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i,j] > 0:
                sum += board[i,j]
    return sum * drawnNum

def updateBoards(boards : list, num : int) -> list:
    for board in boards:
        for i in range(5):
            for j in range(5):
                if board[i,j] == num:
                    board[i,j] = -1
    return boards


def firstWinning_0(boards : list, drawnNums : list) -> int:
    for num in drawnNums:
        boards = updateBoards(boards,num)
        for board in boards:
            if isWinning(board):
                return score(board,num)
    return 'No winner'

def firstWinning(file_name : str) -> int:
    return firstWinning_0(makeBoards(file_name),drawnNums(file_name))

def lastWinning0(boards : list, drawnNums : list) -> int:
    listOfWins = [False] * len(boards)
    for num in drawnNums:
        boards = updateBoards(boards,num)
        for i in range(len(boards)):
            if isWinning(boards[i]):
                listOfWins[i] = True
                if all(listOfWins):
                    return score(boards[i],num)
    return None

def lastWinning(file_name : str) -> int:
    return lastWinning0(makeBoards(file_name),drawnNums(file_name))

print(lastWinning('day4'))
