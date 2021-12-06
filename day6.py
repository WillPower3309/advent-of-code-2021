def calculateNumFish(initialNumList: list, numDays: int) -> int:
    spawnTimer = [0 for _ in range(9)] # array of 9 0s
    numFish = len(initialNumList)
    for num in initialNumList:
        spawnTimer[int(num)] += 1

    for _ in range(numDays):
        numReset = spawnTimer[0]
        for i in range(8):
            spawnTimer[i] = spawnTimer[i + 1]
        spawnTimer[6] += numReset
        spawnTimer[8] = numReset
        numFish += numReset
    return numFish

f = open('input/day6.txt', 'r')
initialState = f.readline()[:-1].split(',')

##################
# PART ONE
##################

print('Part One Solution: %d' % calculateNumFish(initialState, 80))

##################
# PART TWO
##################

print('Part Two Solution: %d' % calculateNumFish(initialState, 256))

