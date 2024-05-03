# WARNING: This implementation is rather slow (1-2 minutes) and inefficient.


def part_one(content):
    """Calculate the 2020th number spoken."""

    while len(content) < 2020:
        if content.count(content[-1]) == 1:
            content.append(0)
        else:
            index = None
            for i in range(0, len(content)-1):
                if content[-1] == content[i]:
                    index = i+1
            content.append(len(content) - index)

    return content[-1]


def part_two(content):
    """
    Calculate the 30000000th number spoken.
    This part takes to long to be efficient, but it still works in
    about 30 seconds.
    """

    numberCounts = {}
    for i, num in enumerate(content):
        if num in numberCounts.keys():
            numberCounts[num][0] += 1
            numberCounts[num][1].append(i+1)
        else:
            numberCounts[num] = [1, [i+1]]

    i = len(content) + 1
    while len(content) < 30000000:
        lastNum = content[-1]

        if numberCounts[lastNum][0] == 1:
            content.append(0)
            numberCounts[0][0] += 1
            numberCounts[0][1].append(i)
        else:
            nextNum = (numberCounts[lastNum][1][-1] -
                       numberCounts[lastNum][1][-2])
            content.append(nextNum)
            if nextNum in numberCounts.keys():
                numberCounts[nextNum][0] += 1
                numberCounts[nextNum][1].append(i)
            else:
                numberCounts[nextNum] = [1, [i]]

        i += 1

    return content[-1]


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [item.strip() for item in content]

    content = content[0].split(',')
    content = [int(num) for num in content]

    res1 = part_one(content.copy())
    print(f'Part One: {res1}')

    res2 = part_two(content.copy())
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
