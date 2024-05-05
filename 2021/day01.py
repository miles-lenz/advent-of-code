def part_one(data):

    count = 0

    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            count += 1

    return count


def part_two(data):

    windows = []

    for i in range(len(data) - 2):
        windows += [data[i] + data[i + 1] + data[i + 2]]

    return part_one(windows)


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [int(item.strip()) for item in data]

    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")


if __name__ == "__main__":
    main()
