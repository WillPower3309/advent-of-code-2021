import copy

BOARD_SIZE = 5

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
        isFound = False
        for i in range(BOARD_SIZE):
            if self.rows[i].check(val) or self.cols[i].check(val):
                isFound = True
        return isFound

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

if len(currBoardRows) == BOARD_SIZE: # if input didnt end with \n
    boards.append(Board(currBoardRows))

##################
# PART ONE
##################

def computeBingo(numbers, boards) -> int:
    for num in numbers:
        for board in boards:
            if board.check(num):
                return board.getUnmarkedSum() * int(num)
    return 0

# pass deepcopied array to avoid pass by reference
# this lets the list of boards be reused for part two
print('Part One Solution: %d' % computeBingo(numbers, copy.deepcopy(boards)))

##################
# PART TWO
##################

def computeLastBingo(numbers, boards) -> int:
    numBoards = len(boards)
    for num in numbers:
        boardsToPop = []
        for i in range(numBoards):
            if boards[i].check(num):
                if numBoards == 1:
                    return(boards[i].getUnmarkedSum() * int(num))
                boardsToPop.append(i)

        for index in reversed(boardsToPop):
            boards.pop(index)
            numBoards -= 1

    return 0

print('Part Two Solution: %d' % (computeLastBingo(numbers, boards)))

