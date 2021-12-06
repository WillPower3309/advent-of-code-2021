import re
import copy

f = open('input/day5.txt', 'r')

coordinatesList = []

buffer = f.readline()[:-1]
while buffer:
    coordinates = [int(i) for i in re.split(r',| -> ', buffer)]
    coordinatesList.append(coordinates)
    buffer = f.readline()[:-1]

def listFromRange(valOne: int, valTwo: int) -> list:
    if valOne > valTwo:
        return list(range(valOne, valTwo - 1, -1))
    return list(range(valOne, valTwo + 1))


##################
# PART ONE
##################

board = {}
numOverlap = 0

for coordinate in coordinatesList:
    xs = listFromRange(coordinate[0], coordinate[2])
    ys = listFromRange(coordinate[1], coordinate[3])

    if len(ys) != len(xs):
        for x in xs:
            for y in ys:
                key = f'{x}-{y}' # fstrings are fastest way to do this
                board[key] = board.get(key, 0) + 1
                if board[key] == 2:
                    numOverlap += 1

print('Part One Solution: %d' % numOverlap)

##################
# PART TWO
##################

board = {}
numOverlap = 0

for coordinate in coordinatesList:
    xs = listFromRange(coordinate[0], coordinate[2])
    ys = listFromRange(coordinate[1], coordinate[3])

    if len(ys) != len(xs):
        for x in xs:
            for y in ys:
                key = f'{x}-{y}' # fstrings are fastest way to do this
                board[key] = board.get(key, 0) + 1
                if board[key] == 2:
                    numOverlap += 1
    else: # diagonal
        for i in range(len(ys)): # could zip() but this is slightly faster :p
            key = f'{xs[i]}-{ys[i]}' # fstrings are fastest way to do this
            board[key] = board.get(key, 0) + 1
            if board[key] == 2:
                numOverlap += 1

print('Part Two Solution: %d' % numOverlap)

