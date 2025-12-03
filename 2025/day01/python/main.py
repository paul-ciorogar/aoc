import sys
import math


def rotateLeft(dial, steps):
    if dial == 0:
        dial = 100 - steps
        return dial, 0

    if dial > steps:
        dial = dial - steps
        return dial, 0

    steps = abs(dial - steps)
    return 0, steps


def rotateRight(dial, steps):
    dial = dial + steps

    if dial > 100:
        steps = dial - 100
        return 0, steps

    if dial == 100:
        return 0, 0

    return dial, 0


count = 0
dial = 50

for line in sys.stdin:
    line = line.strip()
    steps = int(line[1:])
    leftRotation = line[0] == 'L'

    if steps > 100:
        count = count + math.floor(steps/100)
        steps = steps % 100

    while steps != 0:
        if leftRotation:
            dial, steps = rotateLeft(dial, steps)
        else:
            dial, steps = rotateRight(dial, steps)

        if dial == 0:
            count += 1

print(count)
