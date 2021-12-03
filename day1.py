##################
# PART ONE
##################

f = open('input/day1.txt', 'r')

counter = 0
prevInput = float('inf')

buffer = f.readline()
while buffer:
    val = int(buffer[:-1])
    if val > prevInput:
        counter += 1

    prevInput = val
    buffer = f.readline()

print('Part One Solution: %d' % counter)

##################
# PART TWO
##################

buffer = [int(x) for x in open('input/day1.txt', 'r')]
counter = 0
prevSum = float('inf')

for i in range(2, len(buffer)):
    newSum = buffer[i] + buffer[i-1] + buffer[i-2]
    if newSum > prevSum:
        counter += 1
    prevSum = newSum

print('Part Two Solution: %d' % counter)

