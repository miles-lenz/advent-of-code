from itertools import combinations
import numpy as np


def main():

    with open("input.txt") as f:
        data = np.array([list(line.strip()) for line in f])

    part_one, part_two = set(), set()
    for freq in np.unique(data)[np.unique(data) != "."]:

        freq_pos = np.argwhere(data == freq)
        for pos1, pos2 in combinations(freq_pos, 2):

            offsets = [(pos1 - pos2), (pos2 - pos1)]
            for i, anti in enumerate([pos1 + offsets[0], pos2 + offsets[1]]):

                if all(anti >= 0) and all(anti < data.shape):
                    part_one.add(tuple(anti))

                while all(anti >= 0) and all(anti < data.shape):
                    part_two.add(tuple(anti))
                    anti += offsets[i]

            part_two.update(map(tuple, [pos1, pos2]))

    print(f"Part One: {len(part_one)}")
    print(f"Part Two: {len(part_two)}")


if __name__ == "__main__":
    main()
