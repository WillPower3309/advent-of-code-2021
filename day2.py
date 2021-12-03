##################
# PART ONE
##################

f = open('input/day2.txt', 'r')

depth = 0
horiz = 0

buffer = f.readline()
while buffer:
    data = buffer[:-1].split()
    if data[0] == 'forward':
        horiz += int(data[1])
    elif data[0] == 'down':
        depth += int(data[1])
    elif data[0] == 'up':
        depth -= int(data[1])

    buffer = f.readline()

print('Part One Solution: %d' % (depth * horiz))

##################
# PART TWO
##################

f = open('input/day2.txt', 'r')

depth = 0
horiz = 0
aim = 0

buffer = f.readline()
while buffer:
    data = buffer[:-1].split()
    if data[0] == 'forward':
        horiz += int(data[1])
        depth += (aim * int(data[1]))
    elif data[0] == 'down':
        aim += int(data[1])
    elif data[0] == 'up':
        aim -= int(data[1])

    buffer = f.readline()

print('Part Two Solution: %d' % (horiz * depth))

