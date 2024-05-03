def part_one(seatIDs):
    """Find highest seat ID on a boarding pass."""

    maxID = max(seatIDs)

    return maxID


def part_two(seatIDs):
    """Find your own seat ID."""

    seatIDs.sort()

    for i in range(len(seatIDs[:-1])):
        if seatIDs[i+1] - seatIDs[i] > 1:
            mySeat = seatIDs[i] + 1

    return mySeat


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [item.strip() for item in content]

    seatIDs = []

    for seat in content:
        rowNo, colNo = '', ''
        row, col = seat[:7], seat[7:]

        for char in row:
            rowNo += '0' if char == 'F' else '1'

        for char in col:
            colNo += '0' if char == 'L' else '1'

        seatID = int(rowNo, 2) * 8 + int(colNo, 2)
        seatIDs.append(seatID)

    res1 = part_one(seatIDs)
    print(f'Part One: {res1}')

    res2 = part_two(seatIDs)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
