# WARNING: This implementation is rather slow (2-3 minutes) and inefficient.

import numpy as np


def get_neighbors(data, y, x):

    neighbors = []

    # Get height of current position.
    height = ord(data[y, x].replace("S", "a").replace("E", "z"))

    # Get neighbors based on indices adn their height.
    if y > 0:
        n_height = ord(data[y-1, x].replace("S", "a").replace("E", "z"))
        if n_height - height <= 1:
            neighbors.append((y-1, x))
    if x > 0:
        n_height = ord(data[y, x-1].replace("S", "a").replace("E", "z"))
        if n_height - height <= 1:
            neighbors.append((y, x-1))
    if y < data.shape[0] - 1:
        n_height = ord(data[y+1, x].replace("S", "a").replace("E", "z"))
        if n_height - height <= 1:
            neighbors.append((y+1, x))
    if x < data.shape[1] - 1:
        n_height = ord(data[y, x+1].replace("S", "a").replace("E", "z"))
        if n_height - height <= 1:
            neighbors.append((y, x+1))

    return neighbors


def compute_heuristic_cost(data):

    heuristic_cost = np.zeros(data.shape)

    # Get indices of end node.
    ej, ei = np.argwhere(data == "E")[0]

    # Iterate over the data.
    for j in range(data.shape[0]):
        for i in range(data.shape[1]):

            # Compute manhattan distance from current node to end node.
            # This is the heuristic cost.
            heuristic_cost[j, i] = np.abs(ej - j) + np.abs(ei - i)

    return heuristic_cost


def part_one(data):

    # Find the starting position.
    y, x = np.argwhere(data == "S")[0]

    # Initialize the various needed requirements.
    open_ = [(y, x)]
    closed = []
    g = np.empty(data.shape)
    g[:, :], g[y, x] = np.inf, 0
    h = compute_heuristic_cost(data)

    # Perform the A* path finding algorithm.
    while True:

        # Get node with lowest f score in open list.
        lowest_f, lowest_ind = np.inf, None
        for y, x in open_:
            f_score = g[y, x] + h[y, x]
            if f_score < lowest_f:
                lowest_f = f_score
                lowest_ind = (y, x)
        y, x = lowest_ind

        # Check if this node is the end node.
        if data[y, x] == "E":
            break

        # Move current node in closed list.
        open_.remove((y, x))
        closed.append((y, x))

        # Iterate over the neighbors.
        for ny, nx in get_neighbors(data, y, x):

            if (ny, nx) in closed:
                continue

            cost = g[y, x] + 1

            if (ny, nx) in open_ and cost < g[ny, nx]:
                open_.remove((ny, nx))

            if (ny, nx) in closed and cost < g[ny, nx]:
                closed.remove((ny, nx))

            if (ny, nx) not in open_ and (ny, nx) not in closed:
                open_.append((ny, nx))
                g[ny, nx] = cost

    # Return cost to the end node.
    return int(g[np.where(data == "E")][0])


def part_two(data):

    steps = []

    for sy in range(data.shape[0]):

        # Find the starting position with lowest heuristic cost.
        y, x = sy, 0

        # Initialize the various needed requirements.
        open_ = [(y, x)]
        closed = []
        g = np.empty(data.shape)
        g[:, :], g[y, x] = np.inf, 0
        h = compute_heuristic_cost(data)

        # Perform the A* path finding algorithm.
        while True:

            # Get node with lowest f score in open list.
            lowest_f, lowest_ind = np.inf, None
            for y, x in open_:
                f_score = g[y, x] + h[y, x]
                if f_score < lowest_f:
                    lowest_f = f_score
                    lowest_ind = (y, x)
            y, x = lowest_ind

            # Check if this node is the end node.
            if data[y, x] == "E":
                break

            # Move current node in closed list.
            open_.remove((y, x))
            closed.append((y, x))

            # Iterate over the neighbors.
            for ny, nx in get_neighbors(data, y, x):

                if (ny, nx) in closed:
                    continue

                cost = g[y, x] + 1

                if (ny, nx) in open_ and cost < g[ny, nx]:
                    open_.remove((ny, nx))

                if (ny, nx) in closed and cost < g[ny, nx]:
                    closed.remove((ny, nx))

                if (ny, nx) not in open_ and (ny, nx) not in closed:
                    open_.append((ny, nx))
                    g[ny, nx] = cost

        steps.append(int(g[np.where(data == "E")][0]))

    # Return cost to the end node.
    return min(steps)


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Transform the data.
    data = [list(item) for item in data]
    data = np.array(data)

    # Solve part one.
    result1 = part_one(data)

    # Solve part two.
    result2 = part_two(data)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
