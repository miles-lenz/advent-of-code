import re
import numpy as np


def fold(paper, instructions):

    visible_dots = 0
    for i, instr in enumerate(instructions):

        dir_, pos = instr[11:].split("=")
        pos = int(pos)

        if dir_ == "x":
            paper_left, paper_right = paper[:, :pos], paper[:, pos + 1:]
            paper = paper_left + np.flip(paper_right, 1)

        elif dir_ == "y":
            paper_top, paper_bottom = paper[:pos, :], paper[pos + 1:, :]
            paper = paper_top + np.flip(paper_bottom, 0)

        if i == 0:
            visible_dots = paper.sum()

    formatter = {'bool': {0: ' ', 1: '█'}.get}
    letters = "\n" + np.array2string(paper, separator='', formatter=formatter)
    letters = re.sub(r'[\[\]]', ' ', letters)

    return visible_dots, letters


def main():

    with open("input.txt") as f:
        data = f.read().split("\n\n")

    coords, instructions = data[0].split("\n"), data[1].split("\n")
    coords = np.array([coord.split(",") for coord in coords], dtype=int)

    shape = np.flip(np.max(coords, 0)) + 1
    shape[shape % 2 == 0] += 1

    paper = np.zeros(shape, dtype=bool)
    paper[coords[:, 1], coords[:, 0]] = 1

    visible_dots, letters = fold(paper, instructions)

    print(f"Part One: {visible_dots}")
    print(f"Part Two: {letters}")


if __name__ == "__main__":
    main()
