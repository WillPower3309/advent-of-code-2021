f = open('input/day9.txt', 'r')

heightMap = []

buffer = f.readline()
while buffer:
    heightMap.append([int(x) for x in buffer[:-1]])
    buffer = f.readline()

yMax = len(heightMap)
xMax = len(heightMap[0])

##################
# PART ONE
##################

riskLevelSum = 0

# probably faster with BFS
for y in range(yMax):
    for x in range(xMax):
        currPoint = heightMap[y][x]

        if y < yMax - 1 and heightMap[y + 1][x] <= currPoint:
            continue
        if y > 0 and heightMap[y - 1][x] <= currPoint:
            continue
        if x < xMax - 1 and heightMap[y][x + 1] <= currPoint:
            continue
        if x > 0 and heightMap[y][x - 1] <= currPoint:
            continue

        riskLevelSum += currPoint + 1

print('Part One Solution: %d' % riskLevelSum)

##################
# PART TWO
##################
# basically the leetcode island question

import bisect

class partTwo:
    basins = []
    numBasins = 0
    currBasinSize = 0

    def dfs(self, y, x):
        if heightMap[y][x] == 9:
            return

        self.currBasinSize += 1
        heightMap[y][x] = 9 # so it isnt recounted

        if y < yMax - 1:
            self.dfs(y + 1, x)
        if y > 0:
            self.dfs(y - 1, x)
        if x < xMax - 1:
            self.dfs(y, x + 1)
        if x > 0:
            self.dfs(y, x - 1)

    def compute(self):
        for y in range(yMax):
            for x in range(xMax):
                if heightMap[y][x] != 9:
                    self.dfs(y, x)
                    bisect.insort(self.basins, self.currBasinSize)
                    self.numBasins += 1
                    self.currBasinSize = 0

        return self.basins[self.numBasins - 1] * self.basins[self.numBasins - 2] * self.basins[self.numBasins - 3]

print('Part Two Solution: %d' % partTwo().compute())
