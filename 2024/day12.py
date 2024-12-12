from collections import defaultdict
import numpy as np


def find_region_indices(data, i, j, ind, p):

    ind.append([i, j])

    if i + 1 < data.shape[0] and [i + 1, j] not in ind and data[i + 1, j] == p:
        find_region_indices(data, i + 1, j, ind, p)
    if i - 1 >= 0 and [i - 1, j] not in ind and data[i - 1, j] == p:
        find_region_indices(data, i - 1, j, ind, p)
    if j + 1 < data.shape[1] and [i, j + 1] not in ind and data[i, j + 1] == p:
        find_region_indices(data, i, j + 1, ind, p)
    if j - 1 >= 0 and [i, j - 1] not in ind and data[i, j - 1] == p:
        find_region_indices(data, i, j - 1, ind, p)


def calc_perimeter(data, indices, plant):

    perimeter = 0
    for i, j in indices:

        if i + 1 >= data.shape[0] or data[i + 1, j] != plant:
            perimeter += 1
        if i - 1 < 0 or data[i - 1, j] != plant:
            perimeter += 1
        if j + 1 >= data.shape[1] or data[i, j + 1] != plant:
            perimeter += 1
        if j - 1 < 0 or data[i, j - 1] != plant:
            perimeter += 1

    return perimeter


def calc_sides(data, indices, plant):

    log = defaultdict(list)

    indices = sorted(indices, key=lambda ind: (ind[0], ind[1]))

    sides = 0
    for i, j in indices:

        if i + 1 >= data.shape[0] or data[i + 1, j] != plant:
            if not neighbor_contributed(i, j, log, "v"):
                sides += 1
            log[(i, j)].append("v")
        if i - 1 < 0 or data[i - 1, j] != plant:
            if not neighbor_contributed(i, j, log, "^"):
                sides += 1
            log[(i, j)].append("^")
        if j + 1 >= data.shape[1] or data[i, j + 1] != plant:
            if not neighbor_contributed(i, j, log, ">"):
                sides += 1
            log[(i, j)].append(">")
        if j - 1 < 0 or data[i, j - 1] != plant:
            if not neighbor_contributed(i, j, log, "<"):
                sides += 1
            log[(i, j)].append("<")

    return sides


def neighbor_contributed(i, j, log, symbol):

    for x, y in [[i - 1, j], [i,  j - 1]]:
        if (x, y) in log.keys() and symbol in log[(x, y)]:
            return True

    return False


def main():

    with open("input.txt") as f:
        data = np.array([list(line.strip()) for line in f])

    visited, total_price1, total_price2 = [], 0, 0
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):

            if [row, col] in visited:
                continue

            region_indices = []
            find_region_indices(data, row, col, region_indices, data[row, col])

            visited += region_indices

            area = len(region_indices)
            perimeter = calc_perimeter(data, region_indices, data[row, col])
            sides = calc_sides(data, region_indices, data[row, col])

            total_price1 += area * perimeter
            total_price2 += area * sides

    print(f"Part One: {total_price1}")
    print(f"Part Two: {total_price2}")


if __name__ == "__main__":
    main()
