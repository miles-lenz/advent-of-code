import numpy as np

# *** This is by far not the most efficient and cleanest solution.
# *** But it works xD


def is_loop(data, pos):

    row, col = np.argwhere(data == "^")[0]
    data[pos] = "O"

    all_d = ["n", "e", "s", "w"]
    d = "n"

    lim_rows = [0, data.shape[0] - 1]
    lim_cols = [0, data.shape[1] - 1]

    obstacles = []

    while row not in lim_rows and col not in lim_cols:

        last_pos = [row, col]

        if d in ["n", "s"]:
            row += -1 if d == "n" else 1
        if d in ["w", "e"]:
            col += -1 if d == "w" else 1

        if data[row, col] in ["#", "O"]:

            if [row, col, last_pos] in obstacles:
                return True
            obstacles.append([row, col, last_pos])

            row, col = last_pos
            d = all_d[(all_d.index(d) + 1) % 4]

    return False


def main():

    with open("input.txt") as f:
        data = np.array([list(line.strip()) for line in f])

    row, col = np.argwhere(data == "^")[0]

    all_d = ["n", "e", "s", "w"]
    d = "n"

    lim_rows = [0, data.shape[0] - 1]
    lim_cols = [0, data.shape[1] - 1]

    visited = set()
    while row not in lim_rows and col not in lim_cols:

        visited.add((row, col))

        last_pos = [row, col]

        if d in ["n", "s"]:
            row += -1 if d == "n" else 1
        if d in ["w", "e"]:
            col += -1 if d == "w" else 1

        if data[row, col] == "#":
            row, col = last_pos
            d = all_d[(all_d.index(d) + 1) % 4]
    visited.add((row, col))

    loop = 0
    for pos in visited:
        if is_loop(np.copy(data), pos):
            loop += 1

    print(f"Part One: {len(visited)}")
    print(f"Part Two: {loop}")


if __name__ == "__main__":
    main()
