import re
import copy

f = open('input/day5.txt', 'r')

coordinatesList = []
maxX = 0
maxY = 0

buffer = f.readline()[:-1]
while buffer:
    coordinates = [int(i) for i in re.split(r',| -> ', buffer)]
    maxX = max(maxX, coordinates[0])
    maxY = max(maxY, coordinates[1])
    maxX = max(maxX, coordinates[2])
    maxY = max(maxY, coordinates[3])
    coordinatesList.append(coordinates)
    buffer = f.readline()[:-1]

board = [[0]*(maxX + 1) for _ in range(maxY + 1)]

##################
# PART ONE
##################

boardOne = copy.deepcopy(board)
numOverlap = 0

for coordinate in coordinatesList:
    x1 = coordinate[0]
    y1 = coordinate[1]
    x2 = coordinate[2]
    y2 = coordinate[3]

    if(x1 == x2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            boardOne[y][x1] += 1
            if boardOne[y][x1] == 2:
                numOverlap += 1
    elif(y1 == y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            boardOne[y1][x] += 1
            if boardOne[y1][x] == 2:
                numOverlap += 1

print('Part One Solution: %d' % numOverlap)

##################
# PART TWO
##################

numOverlap = 0

for coordinate in coordinatesList:
    x1 = coordinate[0]
    y1 = coordinate[1]
    x2 = coordinate[2]
    y2 = coordinate[3]

    if(x1 == x2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            board[y][x1] += 1
            if board[y][x1] == 2:
                numOverlap += 1
    elif(y1 == y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            board[y1][x] += 1
            if board[y1][x] == 2:
                numOverlap += 1
    else:
        # y = mx + b (m is always 1 or -1 due to 45 degree angle)
        # ... algebra things ... b = [x2y1-x1y2]/[x2-x1]
        m = (y2 - y1) / (x2 - x1)
        b = int(((x2*y1) - (x1*y2)) / (x2-x1))
        for i in range(min(x1, x2), max(x1, x2) + 1):
            board[int((m * i) + b)][i] += 1
            if board[int((m * i) + b)][i] == 2:
                numOverlap += 1

print('Part Two Solution: %d' % numOverlap)

