def part_one(content):
    """Find the num of 1-jolt / 3-jolt differences."""

    difference_1_jolt = 0
    difference_3_jolt = 0

    for i in range(len(content)-1):
        if content[i+1] - content[i] == 1:
            difference_1_jolt += 1
        elif content[i+1] - content[i] == 3:
            difference_3_jolt += 1
        elif content[i+1] - content[i] > 3:
            return False

    return difference_1_jolt * difference_3_jolt


def part_two(content):
    """
    Find the total num of distinct ways you can arrange the adapters.
    Credits: Bradley Sward
    """

    paths = [0] * (max(content) + 1)
    paths[0] = 1

    for index in range(1, max(content) + 1):
        for x in range(1, 4):
            if (index - x) in content:
                paths[index] += paths[index - x]

    return paths[-1]


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [item.strip() for item in content]

    content = [int(x) for x in content]
    content.append(0)
    content.append(max(content)+3)
    content.sort()

    res1 = part_one(content)
    print(f'Part One: {res1}')

    res2 = part_two(content)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
