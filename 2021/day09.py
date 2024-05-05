import numpy as np


def get_neighbors(y, x, data):

    neighbors = []
    coords = []

    if y > 0:
        neighbors.append(data[y - 1, x])
        coords.append((y - 1, x))
    if y < data.shape[0] - 1:
        neighbors.append(data[y + 1, x])
        coords.append((y + 1, x))
    if x > 0:
        neighbors.append(data[y, x - 1])
        coords.append((y, x - 1))
    if x < data.shape[1] - 1:
        neighbors.append(data[y, x + 1])
        coords.append((y, x + 1))

    return np.array(neighbors), coords


def explore_basin(y, x, data, size, visited):

    size += 1
    visited.append((y, x))

    for n, c in zip(*get_neighbors(y, x, data)):

        if n == 9 or c in visited:
            continue

        size = explore_basin(c[0], c[1], data, size, visited)

    return size


def part_one(data):

    sum_ = 0
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):

            neighbors = get_neighbors(y, x, data)[0]
            low_point = np.all(data[y, x] < neighbors)

            if low_point:
                sum_ += data[y, x] + 1

    return sum_


def part_two(data):

    basin_sizes = []
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):

            neighbors, coords = get_neighbors(y, x, data)
            low_point = np.all(data[y, x] < neighbors)

            if low_point:
                basin_size = explore_basin(y, x, data, 0, [])
                basin_sizes.append(basin_size)

    basin_sizes = sorted(basin_sizes)[::-1]
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [list(item.strip()) for item in data]
    data = np.array(data, dtype=int)

    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")


if __name__ == "__main__":
    main()
