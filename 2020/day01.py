def part_one(content):
    """Find the two entries that sum to 2020."""

    for i, num1 in enumerate(content):
        for num2 in content[i+1:]:
            if num1 + num2 == 2020:
                result = num1 * num2
                break

    return result


def part_two(content):
    """Find the three entries that sum to 2020."""

    for i, num1 in enumerate(content):
        for j, num2 in enumerate(content[i+1:]):
            for num3 in content[j+1:]:
                if num1 + num2 + num3 == 2020:
                    result = num1 * num2 * num3
                    break

    return result


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [int(item.strip()) for item in content]

    res1 = part_one(content)
    print(f'Part One: {res1}')

    res2 = part_two(content)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
