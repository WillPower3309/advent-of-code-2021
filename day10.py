charPairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def isOpen(char):
    return char in charPairs

def isValidClose(openingChar, closingChar):
    return openChar in charPairs and charPairs[openingChar] == closingChar

##################
# PART ONE
##################

illegalCharScore = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
errorScore = 0
stack = []

f = open('input/day10.txt', 'r')

buffer = f.readline()[:-1]
while buffer:
    # assess line
    for char in buffer:
        if isOpen(char):
            stack.append(char)
        else:
            openChar = stack.pop()
            if not isValidClose(openChar, char):
                errorScore += illegalCharScore[char]
                break
    stack = []
    buffer = f.readline()[:-1]

print('Part One Solution: %d' % errorScore)

##################
# PART TWO
##################

import bisect

addedCharScore = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

stack = []
autocompleteScores = []

f = open('input/day10.txt', 'r')

buffer = f.readline()[:-1]
while buffer:
    isIncomplete = True
    # assess line
    for char in buffer:
        if isOpen(char):
            stack.append(char)
        else:
            openChar = stack.pop()
            if not isValidClose(openChar, char):
                isIncomplete = False
                break

    if isIncomplete:
        scoreToAdd = 0
        while stack:
            scoreToAdd *= 5
            charToAdd = charPairs[stack.pop()]
            scoreToAdd += addedCharScore[charToAdd]
        bisect.insort(autocompleteScores, scoreToAdd)
    stack = []
    buffer = f.readline()[:-1]

print('Part Two Solution: %d' % autocompleteScores[len(autocompleteScores) // 2])
