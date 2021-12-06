buffer = [str(x[:-1]) for x in open('input/day3.txt', 'r')]
buffer.sort()

BUFFER_LEN = len(buffer)
NUM_DIGITS = len(buffer[0])

##################
# PART ONE
##################

gamma = ''
epsilon = ''

for i in range(NUM_DIGITS):
    numOnes = 0
    for j in range(BUFFER_LEN):
        if buffer[j][i] == '1':
            numOnes += 1
    if numOnes > (BUFFER_LEN / 2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print('Part One Solution: %d' % (int(gamma, 2) * int(epsilon, 2)))

##################
# PART TWO
##################

# returns index of first occurance of 1 (binary search)
def findFirstOne(arr: list, i: int, l: int, r: int) -> int:
    result = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid][i] == '1':
            result = mid
            r = mid - 1
        else:
            l = mid + 1
    return result

oStart = 0
oEnd = BUFFER_LEN - 1
cdStart = 0
cdEnd = BUFFER_LEN - 1

for i in range(NUM_DIGITS):
    if oStart == oEnd:
        break
    firstOneIndex = findFirstOne(buffer, i, oStart, oEnd)
    if firstOneIndex <= ((oStart + oEnd + 1) // 2):
        oStart = firstOneIndex
    else:
        oEnd = firstOneIndex - 1
for i in range(NUM_DIGITS):
    if cdStart == cdEnd:
        break
    firstOneIndex = findFirstOne(buffer, i, cdStart, cdEnd)
    if firstOneIndex <= ((cdStart + cdEnd + 1) // 2):
        cdEnd = firstOneIndex - 1
    else:
        cdStart = firstOneIndex
    
print('Part Two Solution: %d' % (int(buffer[oStart], 2) * int(buffer[cdStart], 2)))

