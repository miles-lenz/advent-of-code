import numpy as np


def get_neighbors(y, x, data):

    neighbors = []

    if y > 0:
        neighbors.append((y - 1, x))
    if y < data.shape[0] - 1:
        neighbors.append((y + 1, x))
    if x > 0:
        neighbors.append((y, x - 1))
    if x < data.shape[1] - 1:
        neighbors.append((y, x + 1))
    if y > 0 and x > 0:
        neighbors.append((y - 1, x - 1))
    if y > 0 and x < data.shape[1] - 1:
        neighbors.append((y - 1, x + 1))
    if y < data.shape[0] - 1 and x > 0:
        neighbors.append((y + 1, x - 1))
    if y < data.shape[0] - 1 and x < data.shape[1] - 1:
        neighbors.append((y + 1, x + 1))

    return neighbors


def simulate_flashes(data):

    total_flashes, simultan_flash_found = 0, False

    step = 0
    while not simultan_flash_found:

        data += 1

        flash_history = np.zeros(data.shape)
        while True:

            flashes = np.zeros(data.shape)
            flashes[np.where(data > 9)] = 1
            flashes = np.logical_xor(flashes, flash_history)

            flashes_coords = np.where(flashes)
            flash_history[flashes_coords] = 1

            if step < 100:
                total_flashes += len(flashes_coords[0])

            if len(flashes_coords[0]) == 0:
                break

            for y, x in zip(*flashes_coords):
                neighbors = get_neighbors(y, x, data)
                for n_y, n_x in neighbors:
                    data[n_y, n_x] += 1

        data[data > 9] = 0

        if np.all(data == 0):
            simultan_flash_found = True

        step += 1

    return total_flashes, step


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [list(item.strip()) for item in data]
    data = np.array(data, dtype=int)

    total_flashes, simultan_flashes = simulate_flashes(data)

    print(f"Part One: {total_flashes}")
    print(f"Part Two: {simultan_flashes}")


if __name__ == "__main__":
    main()
