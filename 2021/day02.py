def part_one(data):

    vals = [0, 0]  # horizontal position, depth
    for command in data:

        direction, amount = command.split(" ")
        amount = int(amount)

        if direction == "forward":
            vals[0] += amount
        elif direction == "down":
            vals[1] += amount
        elif direction == "up":
            vals[1] -= amount

    return vals[0] * vals[1]


def part_two(data):

    vals = [0, 0, 0]  # horizontal position, depth, aim
    for command in data:

        direction, amount = command.split(" ")
        amount = int(amount)

        if direction == "forward":
            vals[0] += amount
            vals[1] += vals[2] * amount
        elif direction == "down":
            vals[2] += amount
        elif direction == "up":
            vals[2] -= amount

    return vals[0] * vals[1]


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")


if __name__ == "__main__":
    main()
