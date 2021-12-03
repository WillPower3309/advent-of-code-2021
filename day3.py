##################
# PART ONE
##################

buffer = [str(x[:-1]) for x in open('input/day3.txt', 'r')]
bufferLen = len(buffer)
gamma = ''
epsilon = ''

for i in range(len(buffer[0])):
    numOnes = 0
    for j in range(bufferLen):
        if buffer[j][i] == '1':
            numOnes += 1
    if numOnes > (bufferLen / 2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print('Part One Solution: %d' % (int(gamma, 2) * int(epsilon, 2)))

##################
# PART TWO
##################

