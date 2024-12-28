import numpy as np

with open('calendar_2024/data/day4.txt') as file:
    M = np.array([[ch for ch in line.strip()] for line in file])
print(M)
num = 0
check_obj = ['X','M','A','S']
check_rev = check_obj.reverse()
for i in range(M.shape[0]):
    for j in range(M.shape[1]): # zašto nije htelo M[0].size?
        # check for x
        if M[i,j] == 'X':
            if M[i,j-3:j+1] == check_rev: # <-
                num += 1
                continue
            if M[i,j:j+4] == check_obj: # ->
                num += 1
                continue
            if M[i-3:i+1,j] == check_rev: # ^
                num += 1
                continue
            if M[i:i+4,j] == check_obj: # v
                num += 1
                continue
            ... # dijagonale numpy