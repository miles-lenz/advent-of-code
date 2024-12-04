def part_one(bags):
    """Count bags that can eventually contain at least one shiny gold bag."""

    possibleColors = set()

    colorsToCheck = ['shiny gold']
    while colorsToCheck:
        color = colorsToCheck.pop(0)
        for key, value in bags.items():
            if value[0] is not None and color in [x[1] for x in value]:
                possibleColors.add(key)
                colorsToCheck.append(key)

    return len(possibleColors)


def part_two(bags):
    """Find all individual bags inside your single shiny gold bag."""

    def getBagCount(color):
        total = 0
        for amount, col in bags[color]:
            if not col:
                return 1
            total += amount * getBagCount(col)

        return total + 1

    result = getBagCount('shiny gold') - 1

    return result


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [item.strip() for item in content]

    bags = {}

    for line in content:
        mainBag = line.split(' bags contain ')[0]
        contBags = line.split('contain ')[1].split(', ')
        for i, bag in enumerate(contBags):
            if bag == 'no other bags.':
                contBags[i] = (None, None)
            else:
                bag = bag.split(' ')[:-1]
                bag = (int(bag[0]), ' '.join(bag[1:3]))
                contBags[i] = bag
        bags[mainBag] = contBags

    res1 = part_one(bags)
    print(f'Part One: {res1}')

    res2 = part_two(bags)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
