import re
import copy

f = open('input/day5.txt', 'r')

coordinatesList = []
maxX = 0
maxY = 0

buffer = f.readline()[:-1]
while buffer:
    coordinates = [int(i) for i in re.split(r',| -> ', buffer)]
    maxX = max(maxX, coordinates[0], coordinates[2])
    maxY = max(maxY, coordinates[1], coordinates[3])
    coordinatesList.append(coordinates)
    buffer = f.readline()[:-1]

board = [[0]*(maxX + 1) for _ in range(maxY + 1)]

def listFromRange(valOne, valTwo) -> list:
    if valOne > valTwo:
        return list(range(valOne, valTwo - 1, -1))
    return list(range(valOne, valTwo + 1))


##################
# PART ONE
##################

boardOne = copy.deepcopy(board)
numOverlap = 0

for coordinate in coordinatesList:
    xs = listFromRange(coordinate[0], coordinate[2])
    ys = listFromRange(coordinate[1], coordinate[3])

    if len(ys) != len(xs):
        for y in ys:
            for x in xs:
                boardOne[y][x] += 1
                if boardOne[y][x] == 2:
                    numOverlap += 1

print('Part One Solution: %d' % numOverlap)

##################
# PART TWO
##################

numOverlap = 0

for coordinate in coordinatesList:
    xs = listFromRange(coordinate[0], coordinate[2])
    ys = listFromRange(coordinate[1], coordinate[3])

    if len(ys) != len(xs):
        for y in ys:
            for x in xs:
                board[y][x] += 1
                if board[y][x] == 2:
                    numOverlap += 1
    else: # diagonal
        for i in range(len(ys)):
            board[ys[i]][xs[i]] += 1
            if board[ys[i]][xs[i]] == 2:
                numOverlap += 1

print('Part Two Solution: %d' % numOverlap)

