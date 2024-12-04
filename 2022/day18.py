from itertools import product
import numpy as np


def dfs(cubes, pos, n_coords):

    is_ap = True

    # Initialize the needed requirements.
    stack = [pos]
    visited = np.zeros(cubes.shape)

    # Start the search.
    while len(stack) != 0:

        # Get current position.
        x, y, z = stack.pop(0)

        # Set position as visited.
        visited[x, y, z] = 1

        # Iterate over the neighbors.
        for i, j, k in n_coords:

            # Add unvisited empty cube neighbors to stack.
            try:
                if not visited[x+i, y+j, z+k] and not cubes[x+i, y+j, z+k]:
                    if (x+i, y+j, z+k) not in stack:
                        stack.append((x+i, y+j, z+k))
            except IndexError:
                pass

    # Check if was possible to reach the border.
    cond1 = np.any(visited[0, :, :]) or np.any(visited[-1, :, :])
    cond2 = np.any(visited[:, 0, :]) or np.any(visited[:, -1, :])
    cond3 = np.any(visited[:, :, 0]) or np.any(visited[:, :, -1])
    if cond1 or cond2 or cond3:
        is_ap = False

    # ...
    not_ap = []
    if not is_ap:
        for x, y, z in product(*[range(visited.shape[i]) for i in range(3)]):
            if visited[x, y, z]:
                not_ap.append((x, y, z))

    return is_ap, not_ap


def get_air_pocket_sides(cubes, n_coords):

    sides = 0
    all_not_air_pockets = []

    # Iterate over the complete array.
    for x, y, z in product(*[range(cubes.shape[i]) for i in range(3)]):

        # Check if current cube is empty.
        if not cubes[x, y, z]:

            # ...
            if (x, y, z) not in all_not_air_pockets:
                is_ap, not_ap = dfs(cubes, (x, y, z), n_coords)
                all_not_air_pockets += not_ap
            else:
                is_ap = False

            if is_ap:

                # Get amount of cube sides that air pocket is touching.
                for i, j, k in n_coords:
                    if cubes[x+i, y+j, z+k]:
                        sides += 1

    return sides


def simulate(coords, part_two):

    # Get highest values for x, y and z coordinates.
    x, y, z = 0, 0, 0
    for cx, cy, cz in coords:

        # Replace coordinate if it is higher.
        x = cx if cx > x else x
        y = cy if cy > y else y
        z = cz if cz > z else z

    # Place the cubes.
    cubes = np.zeros((x+1, y+1, z+1))
    for cx, cy, cz in coords:
        cubes[cx, cy, cz] = 1

    # Initialize relative coordinates of neighbors.
    n_coords = [
        (0, 0, 1), (0, 0, -1),
        (0, 1, 0), (0, -1, 0),
        (1, 0, 0), (-1, 0, 0)
    ]

    # Find all sides that are not connected to another cube.
    sides = 0
    for cx, cy, cz in coords:
        for i, j, k in n_coords:

            # Check the neighbor.
            try:

                # Increment amount of sides if there is no neighbor.
                if not cubes[cx+i, cy+j, cz+k]:
                    sides += 1

            except IndexError:

                # Increment sides since the cube is at the edge and
                # therefore this side is not connected to other cubes.
                sides += 1

    # Find all air pockets and adjust the sides result.
    if part_two:
        sides -= get_air_pocket_sides(cubes, n_coords)

    return sides


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Transform data.
    data = [item.split(",") for item in data]
    data = np.array(data, dtype=int)

    # Solve part one.
    result1 = simulate(data, part_two=False)

    # Solve part two.
    result2 = simulate(data, part_two=True)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
