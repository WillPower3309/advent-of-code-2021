f = open('input/day6.txt', 'r')
initialState = f.readline()[:-1].split(',')

##################
# PART ONE
##################

spawnTimer = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}
numFish = 0

numFish = len(initialState)
for num in initialState:
    spawnTimer[int(num)] += 1

for _ in range(80):
    numReset = spawnTimer[0]
    for i in range(8):
        spawnTimer[i] = spawnTimer[i + 1]
    spawnTimer[6] += numReset
    spawnTimer[8] = numReset
    numFish += numReset

print('Part One Solution: %d' % numFish)

##################
# PART TWO
##################

spawnTimer = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}
numFish = 0

f = open('input/day6.txt', 'r')
initialState = f.readline()[:-1].split(',')

numFish = len(initialState)
for num in initialState:
    spawnTimer[int(num)] += 1

for _ in range(256):
    numReset = spawnTimer[0]
    for i in range(8):
        spawnTimer[i] = spawnTimer[i + 1]
    spawnTimer[6] += numReset
    spawnTimer[8] = numReset
    numFish += numReset

print('Part Two Solution: %d' % numFish)

