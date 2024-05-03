def part_one(content):
    """Count the trees you would encounter on the slope."""

    treeCounter = 0

    i, j = 0, 0
    n = len(content[0])
    while i < len(content):
        if content[i][j % n] == '#':
            treeCounter += 1
        i += 1
        j += 3

    return treeCounter


def part_two(content):
    """Count trees for multiple slopes and multiply result."""

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    treeCounter = [0] * len(slopes)

    for slopeNo, slope in enumerate(slopes):
        i, j = 0, 0
        n = len(content[0])
        while i < len(content):
            if content[i][j % n] == '#':
                treeCounter[slopeNo] += 1
            i += slope[1]
            j += slope[0]

    result = 1
    for num in treeCounter:
        result *= num

    return result


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [item.strip() for item in content]

    res1 = part_one(content)
    print(f'Part One: {res1}')

    res2 = part_two(content)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
