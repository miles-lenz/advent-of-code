import re
import math


def calc_possibilities(times, records, part_two):

    if part_two:
        times = [int("".join([str(t) for t in times]))]
        records = [int("".join([str(r) for r in records]))]

    result = 1
    for t, r in zip(times, records):

        x1 = -(-t/2) - math.sqrt((-t/2)**2 - r)
        x1 = int(x1 + 1) if x1.is_integer() else math.ceil(x1)

        x2 = -(-t/2) + math.sqrt((-t/2)**2 - r)
        x2 = int(x2 - 1) if x2.is_integer() else math.floor(x2)

        result *= x2 - x1 + 1

    return result


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [re.findall(r"\b\d+\b", item) for item in data]

    times, records = [int(x) for x in data[0]], [int(x) for x in data[1]]

    print(f"Part One: {calc_possibilities(times, records, False)}")
    print(f"Part Two: {calc_possibilities(times, records, True)}")


if __name__ == "__main__":
    main()
