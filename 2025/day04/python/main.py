import sys


def takeAvailable(data):
    toRemove = []
    processFirstRow(data, toRemove)

    for row in range(1, (len(data) // rowLength)-1):
        processFirstElement(data, row, toRemove)
        processElements(data, row, toRemove)
        processLastElement(data, row, toRemove)

    processLastRow(data, toRemove)

    for index in toRemove:
        data[index] = 0


def part1(data):
    initial = sum(data)
    takeAvailable(data)
    return initial - sum(data)


def processFirstRow(data, toRemove):
    # first element has only three neighbors
    toRemove.append(0)

    for index, element in enumerate(data[1:rowLength-1]):
        index = index+1

        if element == 0:
            continue
        neighbors = (data[index-1]                  # left
                     + data[index+1]                # right
                     + data[index+rowLength-1]      # bottom left
                     + data[index+rowLength]        # bottom
                     + data[index+rowLength+1])     # bottom right

        if neighbors < 4:
            toRemove.append(index)

    # last one has only three neighbors
    toRemove.append(rowLength-1)


def processLastRow(data, toRemove):
    ri = len(data) - rowLength

    # first element has only three neighbors
    toRemove.append(ri)

    for index, element in enumerate(data[ri + 1: -1]):
        index = ri + index + 1
        if data[index] == 0:
            continue
        neighbors = (data[index-1]                      # left
                     + data[index - rowLength - 1]      # top left
                     + data[index - rowLength]          # top
                     + data[index - rowLength + 1]      # top left
                     + data[index + 1])                 # right

        if neighbors < 4:
            toRemove.append(index)

    # last one has only three neighbors
    toRemove.append(len(data)-1)


def processElements(data, row, toRemove):
    ri = row*rowLength+1  # relative index

    # skip the last one we handle it in the next function
    for index, element in enumerate(data[ri:ri+rowLength-2]):
        index = index+ri

        if element == 0:
            continue

        neighbors = (data[index-1]                  # left
                     + data[index+1]                # right
                     + data[index - rowLength]      # top
                     + data[index - rowLength - 1]  # top left
                     + data[index - rowLength + 1]  # top right
                     + data[index + rowLength]      # bottom
                     + data[index + rowLength - 1]  # bottom left
                     + data[index + rowLength + 1])  # bottom right

        if neighbors < 4:
            toRemove.append(index)


def processFirstElement(data, row, toRemove):
    ri = row*rowLength  # relative index

    if data[ri] == 0:
        return

    neighbors = (data[ri-rowLength]         # top
                 + data[ri-rowLength+1]     # top right
                 + data[ri+1]               # right
                 + data[ri+rowLength]       # bottom
                 + data[ri+rowLength+1])    # bottom right

    if neighbors < 4:
        toRemove.append(ri)


def processLastElement(data, row, toRemove):
    ri = row * rowLength + rowLength - 1  # relative index

    if data[ri] == 0:
        return

    neighbors = (data[ri - rowLength]         # top
                 + data[ri - rowLength - 1]   # top left
                 + data[ri - 1]               # left
                 + data[ri + rowLength]       # bottom
                 + data[ri + rowLength-1])    # bottom left

    if neighbors < 4:
        toRemove.append(ri)


def leftNeighbor(data, index):
    if index % (rowLength+1) == 0 or index == 0:
        return 0
    return data[index-1]


def rightNeighbor(data, index):
    if index % rowLength == 0:
        return 0
    return data[index+1]


def part2(data):
    initial = sum(data)
    last = initial

    while True:
        takeAvailable(data)
        current = sum(data)
        if current == last:
            break
        last = current

    return initial - last


lines = sys.stdin.readlines()

data = []

rowLength = len(lines[0].strip())

for line in lines:
    for c in line.strip():
        data.append(1 if c == '@' else 0)

print(f'part 1: {part1(data.copy())}')
print(f'part 2: {part2(data)}')
