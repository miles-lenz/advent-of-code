def part_one(content):
    """Count questions answered with yes from at least one for each group."""

    groups = []

    group = []
    for line in content:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)

    counts = []
    for group in groups:
        questions = set()
        for answer in group:
            for letter in answer:
                questions.add(letter)
        counts.append(len(questions))

    result = sum(counts)

    return result


def part_two(content):
    """Count questions answered with yes from everyone for each group."""

    groups = []

    group = []
    for line in content:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)

    counts = []
    for group in groups:
        sets = []
        for answer in group:
            letterSet = set()
            for letter in answer:
                letterSet.add(letter)
            sets.append(letterSet)

        if len(sets) == 1:
            intersectionSet = sets[0]
        else:
            intersectionSet = sets[0].intersection(*sets[1:])
        counts.append(len(intersectionSet))

    result = sum(counts)

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
