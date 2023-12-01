with open('data/day5.txt') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split()
        lines[i].remove('->')
        lines[i][0] = lines[i][0].split(',')
        lines[i][1] = lines[i][1].split(',')
        for k in range(2):
            for j in range(2):
                lines[i][k][j] = int(lines[i][k][j])
            lines[i][k] = tuple(lines[i][k])
# kraj čitanja

s = [[(0,9),(5,9)],[(8,0),(0,8)],[(9,4),(3,4)],[(2,2),(2,1)],[(7,0),(7,4)],[(6,4),(2,0)],[(0,9),(2,9)],[(3,4),(1,4)],[(0,0),(8,8)],[(5,5),(8,2)]]

import numpy as np
def vents(s : list) -> int:
    maxX = 0
    maxY = 0
    for par1,par2 in s:
        if max(par1[0],par2[0]) > maxX:
            maxX = max(par1[0],par2[0])
        if max(par1[1],par2[1]) > maxY:
            maxY = max(par1[1],par2[1])
    board = np.zeros((maxX + 1 , maxY + 1),dtype=int)
    for par1,par2 in s:
        x1 = par1[0]
        y1 = par1[1]
        x2 = par2[0]
        y2 = par2[1]

        if x1 == x2:
            i = x1
            for j in range(min(y1,y2),max(y1,y2)+1):
                board[j,i] += 1
        elif y1 == y2:
            j = y1
            for i in range(min(x1,x2),max(x1,x2)+1):
                board[j,i] += 1
        else: # part 2 extension
            if (y2-y1)/(x2-x1) == 1: # if k = 1
                for i in range(max(x1,x2)-min(x1,x2) + 1):
                    xz = min(x1,x2)
                    yz = min(y1,y2)
                    board[min(y1,y2) + i, min(x1,x2) + i] += 1
            elif (y2-y1)/(x2-x1) == -1: # if k = -1
                for i in range(max(x1,x2)-min(x1,x2) + 1):
                    xz = min(x1,x2)
                    yz = min(y1,y2)
                    board[max(y1,y2) - i, min(x1,x2) + i] += 1
        # print(board,'\n')
    counter = 0
    for i in range(maxX+1):
        for j in range(maxY+1):
            if board[i,j] >= 2:
                counter += 1
    return counter

print(vents(lines))