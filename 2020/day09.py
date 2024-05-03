def part_one(content):
    """Find the first number that does not follow the rules."""

    def checkSum(i, number):
        numbers = content[i-25:i]
        for n, num1 in enumerate(numbers):
            for num2 in numbers[n+1:]:
                if int(num1) + int(num2) == int(number):
                    return True
        return False

    i = 25
    for number in content[25:]:
        if not checkSum(i, number):
            break
        else:
            i += 1

    return content[i]


def part_two(content, number):
    """Find a contiguous set of at least two numbers."""

    content = [int(num) for num in content]
    number = int(number)

    i = 0
    j = i + 2
    while True:
        if sum(content[i:j]) == number:
            break
        elif sum(content[i:j]) < number:
            j += 1
        else:
            i += 1
            j = i + 2

    result = min(content[i:j]) + max(content[i:j])

    return result


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [item.strip() for item in content]

    res1 = part_one(content)
    print(f'Part One: {res1}')

    res2 = part_two(content, res1)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
