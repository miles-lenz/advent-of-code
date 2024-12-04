def part_one(content):
    """Find the amount of valid passwords."""

    validPasswords = 0

    for line in content:
        rule = line.split(':')[0]
        char = rule.split(' ')[1]
        amount = rule.split(' ')[0]
        minAmount = int(amount.split('-')[0])
        maxAmount = int(amount.split('-')[1])
        pw = line.split(': ')[1]

        if pw.count(char) >= minAmount and pw.count(char) <= maxAmount:
            validPasswords += 1

    return validPasswords


def part_two(content):
    """Find the amount of valid passwords with new rules."""

    validPasswords = 0

    for line in content:
        rule = line.split(':')[0]
        char = rule.split(' ')[1]
        indices = rule.split(' ')[0]
        firstIndex = int(indices.split('-')[0])-1
        secondIndex = int(indices.split('-')[1])-1
        pw = line.split(': ')[1]

        if ((pw[firstIndex] == char and pw[secondIndex] != char) or
                (pw[firstIndex] != char and pw[secondIndex] == char)):
            validPasswords += 1

    return validPasswords


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
