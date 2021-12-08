f = open('input/day7.txt', 'r')
buffer = f.readline()[:-1].split(',')

vals = [int(x) for x in buffer]
vals.sort()
numVals = len(vals)

##################
# PART ONE
##################

currFuel = sum(x - vals[0] for x in vals)
leastFuel = currFuel
valsIndex = 1

for pos in range(vals[0] + 1, vals[numVals - 1]):
    numEqual = 0
    while vals[valsIndex] < pos:
        valsIndex += 1
    numLess = valsIndex
    while vals[valsIndex] == pos:
        numEqual += 1
        valsIndex += 1
    numGreater = numVals - valsIndex

    currFuel += numLess - numEqual - numGreater
    leastFuel = min(leastFuel, currFuel)

print('Part One Solution: %d' % leastFuel)

