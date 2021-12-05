BOARD_SIZE = 5

##################
# PART ONE
##################

class BVector: # board vector
    def __init__(self, inputVals: []) -> None:
        self.vals = {}
        self.numChecked = 0
        for val in inputVals:
            self.vals[val] = False

    def check(self, val: str) -> bool:
        if val in self.vals:
            self.vals[val] = True
            self.numChecked += 1
        return self.numChecked == BOARD_SIZE

    def getUnmarkedSum(self) -> int:
        unmarkedSum = 0
        for k, v in self.vals.items():
            if not v:
                unmarkedSum += int(k)
        return unmarkedSum

class Board:
    def __init__(self, inputRows: []) -> None:
        self.rows = []
        self.cols = []
        for i in range(BOARD_SIZE):
            self.rows.append(BVector(inputRows[i]))
            self.cols.append(BVector([row[i] for row in inputRows]))

    def check(self, val: str) -> bool:
        isFinished = False
        for i in range(BOARD_SIZE):
            if self.rows[i].check(val) or self.cols[i].check(val):
                isFinished = True
        return isFinished

    def getUnmarkedSum(self) -> int:
        sum = 0
        for row in self.rows:
            sum += row.getUnmarkedSum()
        return sum

f = open('input/day4.txt', 'r')

numbers = f.readline()[:-1].split(',')
boards = []

# populate boards
f.readline() # skip empty line
buffer = f.readline()
currBoardRows = []
while buffer:
    if buffer == '\n':
        boards.append(Board(currBoardRows))
        currBoardRows = []
    else:
        row = ([val for val in buffer[:-1].split(' ') if val != ''])
        currBoardRows.append(row)
    buffer = f.readline()

# check for bingo
for num in numbers:
    for board in boards:
        if board.check(num):
            print('Part One Solution: %d' % (board.getUnmarkedSum() * int(num)))
            exit()

