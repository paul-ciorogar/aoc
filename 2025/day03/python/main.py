import sys


lines = sys.stdin.readlines()


def calculateJolts(data):
    left = data[0]
    right = data[1]
    i = 2

    while i < len(data):
        if left < right:
            left = right
            right = data[i]
        if right < data[i]:
            right = data[i]
        i += 1

    return int(left + right)


def calculateJolts2(data):
    result = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    index = 0
    end = -11

    # print(data)

    while end < 0:
        if len(data) - index == abs(end):
            result = copyRest(result, 11 + end, data[index:])
            break
        i, c = max(enumerate(data[index:end]), key=lambda x: x[1])
        result[11 + end] = c
        end += 1
        index += i+1

    if end == 0:
        result[11] = max(data[index:])

    # print(int(''.join(result)))

    return int(''.join(result))


def copyRest(dest, index, data):
    for i, c in enumerate(data):
        dest[index + i] = c
    return dest


def part1(lines):
    result = 0
    for line in lines:
        result += calculateJolts(line.strip())
    # print(f'id: {id} left: {left} right: {right}')

    return result


def part2(lines):
    result = 0
    for line in lines:
        result += calculateJolts2(line.strip())
    # print(f'id: {id} left: {left} right: {right}')

    return result


print(f'part 1: {part1(lines)}')
print(f'part 2: {part2(lines)}')
