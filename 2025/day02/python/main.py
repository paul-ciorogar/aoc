import sys
import textwrap


data = sys.stdin.read().split(',')


def parseIdRange(data):
    parts = data.split('-')
    return range(int(parts[0]), int(parts[1]) + 1)


def part1(data):
    result = 0
    for element in data:
        idRange = parseIdRange(element)

        for i in idRange:
            id = str(i)
            if len(id) % 2 != 0:
                continue
            middle = len(id) // 2
            left = id[:middle]
            right = id[middle:]
            if left == right:
                result += i
                # print(f'id: {id} left: {left} right: {right}')
    return result


def isValid(id):
    length = len(id) // 2 + 1
    for i in range(1, length):
        parts = textwrap.wrap(id, i)
        allSame = all(x == parts[0] for x in parts)
        if allSame:
            # print(f'id: {id} parts: {parts}')
            return True

    return False


def part2(data):
    result = 0
    for element in data:
        idRange = parseIdRange(element)

        for i in idRange:
            id = str(i)
            if isValid(id):
                result += i

    return result


print(f'part 1: {part1(data)}')
print(f'part 2: {part2(data)}')
