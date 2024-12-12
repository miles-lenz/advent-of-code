from collections import defaultdict


def main():

    with open("input.txt") as f:
        disk_map = [int(item) for item in f.readline()]

    blocks, id_ = [], 0
    for i, num in enumerate(disk_map):
        blocks += [str(id_)] * num if i % 2 == 0 else ["."] * num
        id_ += 1 if i % 2 == 0 and i != len(disk_map) - 1 else 0

    checksum1, reverse_index = 0, len(blocks) - 1
    for i, num in enumerate(blocks):

        if i > reverse_index:
            break

        if num == ".":
            checksum1 += i * int(blocks[reverse_index])
            reverse_index -= 1
            while blocks[reverse_index] == ".":
                reverse_index -= 1

        else:
            checksum1 += i * int(num)

    files, spaces = defaultdict(list), []
    id_, index = 0, 0
    for i, num in enumerate(disk_map):
        if i % 2 == 0:
            files[id_] = (index, index + num)
            id_ += 1
        elif num != 0:
            spaces.append((index, index + num))
        index += num
    id_ -= 1

    while id_ >= 0:

        len_file = files[id_][1] - files[id_][0]
        for i, space in enumerate(spaces):

            len_space = space[1] - space[0]
            if len_file > len_space or files[id_][0] < space[0]:
                continue

            diff = len_space - len_file
            files[id_] = (space[0], space[1] - diff)

            if diff == 0:
                spaces.pop(i)
            else:
                spaces[i] = (space[1] - diff, space[1])

            break

        id_ -= 1

    checksum2 = 0
    for num, range_ in files.items():
        for i in range(*range_):
            checksum2 += num * i

    print(f"Part One: {checksum1}")
    print(f"Part Two: {checksum2}")


if __name__ == "__main__":
    main()
