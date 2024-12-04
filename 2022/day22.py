import re
import numpy as np


def transform(data):

    # Extract path from data.
    path = data[-1]
    data = data[:-2]

    # Transform path into list.
    path = re.split(r"(\d+)", path)[1:-1]

    # Get the maximum width of the map.
    max_width = 0
    for line in data:
        if len(line) > max_width:
            max_width = len(line)

    # Create a map based on remaining data information.
    map_ = np.zeros((len(data), max_width), dtype=str)
    map_[:, :] = ""
    for j, line in enumerate(data):
        for i, symbol in enumerate(line):
            map_[j, i] = symbol

    return map_, path


def get_direction(direction_ind):

    if direction_ind == 0:
        return [-1, 0]
    if direction_ind == 1:
        return [0, 1]
    if direction_ind == 2:
        return [1, 0]
    if direction_ind == 3:
        return [0, -1]

    raise Exception("Unknown direction index.")


def get_new_pos(map_, pos, direction):

    pos = np.copy(pos)

    # Repeat process until new position is valid.
    while True:

        # Calculate new coordinates.
        j, i = pos[0] + direction[0], pos[1] + direction[1]

        # Avoid index errors.
        if i < 0:
            i = map_.shape[1]-1
        if j < 0:
            j = map_.shape[0]-1
        if i >= map_.shape[1]:
            i = 0
        if j >= map_.shape[0]:
            j = 0

        # Break if new position is valid.
        if map_[j, i] in [".", "#"]:
            break

        pos = np.array([j, i])

    return np.array([j, i])


def move(map_, pos, direction, steps):

    # Move one step at the time.
    for _ in range(int(steps)):

        # Calculate new position.
        new_pos = get_new_pos(map_, pos, direction)

        # Check if wall is hit.
        if map_[new_pos[0], new_pos[1]] == "#":
            break

        pos = new_pos

    return pos


def part_one(map_, path):

    # Initialize position and direction.
    pos = np.array([0, np.where(map_[0] == ".")[0][0]])
    direction_ind = 1

    # Execute the path instructions.
    for instruction in path:
        instruction: str = instruction

        # Movement.
        if instruction.isdigit():
            direction = get_direction(direction_ind)
            pos = move(map_, pos, direction, instruction)

        # Rotation.
        else:
            direction_ind += 1 if instruction == "R" else -1
            direction_ind = direction_ind % 4

    return 1000*(pos[0]+1) + 4*(pos[1]+1) + direction_ind-1


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.replace("\n", "") for item in data]

    # Transform input data into useful data structures.
    map_, path = transform(data)

    # Solve part one.
    result1 = part_one(map_, path)

    # Print the results for the day.
    print(f"Part One: {result1}")


if __name__ == "__main__":
    main()
