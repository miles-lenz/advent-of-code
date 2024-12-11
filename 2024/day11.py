import math
from collections import defaultdict


def main():

    with open("input.txt") as f:
        data = [int(num) for num in f.readline().split(" ")]

    counts = defaultdict(int)
    for num in data:
        counts[num] += 1

    blinks = 75
    for blink in range(blinks):

        new_counts = defaultdict(int)
        for num, count in counts.items():

            if num == 0:
                new_counts[1] += count
                continue

            len_num = int(math.log10(num)) + 1
            if len_num % 2 == 0:
                N = 10 ** (len_num / 2)
                new_counts[num // N] += count
                new_counts[num % N] += count
                continue

            new_counts[num * 2024] = count

        counts = new_counts

        if blink == 24:
            part_one = sum(counts.values())
    part_two = sum(counts.values())

    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
