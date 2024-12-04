import numpy as np


def create_shape(shape_coords):

    # Iterate over the coordinates and get the height
    # of the shape.
    height = 0
    for y, _ in shape_coords:
        if y > height:
            height = y

    # Create the initial shape.
    shape = np.zeros((height+1, 7), dtype=str)
    shape[:, :] = "."

    # Fill in the shape.
    for y, x in shape_coords:
        shape[y, x] = "@"

    return shape


def add_shape(shape_ind, map_):

    # Define all shapes.
    shapes = [
        [(0, 2), (0, 3), (0, 4), (0, 5)],
        [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)],
        [(0, 4), (1, 4), (2, 4), (2, 3), (2, 2)],
        [(0, 2), (1, 2), (2, 2), (3, 2)],
        [(0, 2), (0, 3), (1, 2), (1, 3)]
    ]

    # Remove rows which contain only air starting from the top
    # until you find one that contains a rock.
    while np.all(map_[0, :] == "."):
        map_ = np.delete(map_, 0, 0)
        if map_.size == 0:
            break

    # Add three rows of air to the top of the map.
    rows_of_air = np.zeros((3, 7), dtype=str)
    rows_of_air[:, :] = "."
    map_ = np.vstack((rows_of_air, map_))

    # Add the shape on top of the map.
    shape = create_shape(shapes[shape_ind])
    map_ = np.vstack((shape, map_))

    return map_, len(shapes[shape_ind])


def horizontal_movement_possible(map_, direction, shape_size):

    # Let n be the number of parts that were already checked.
    n = 0

    # Iterate over the map and check each part of the rock.
    for j in range(map_.shape[0]):
        for i in range(map_.shape[1]):

            # Check if a rock is at the current position.
            if map_[j, i] == "@":

                n += 1

                # Check if moving the rock would case any problems.
                try:
                    cond1 = map_[j, i+direction] in [".", "@"]
                    cond2 = i+direction >= 0
                    if cond1 and cond2:
                        continue
                except IndexError:
                    pass

                return False

            # Check if all parts were discovered.
            if n == shape_size:
                return True

    return True


def move_horizontally(map_, direction, shape_size):

    # Let n be the number of parts that were already checked.
    n = 0

    # Iterate over the map and save coordinates of the rock parts.
    indices = []
    for j in range(map_.shape[0]):
        for i in range(map_.shape[1]):

            # Check if a rock is at the current position.
            if map_[j, i] == "@":

                n += 1

                # Save coordinates of the new rock part.
                indices.append((j, i+direction))

            # Check if all parts were discovered.
            if n == shape_size:
                break
        # Check if all parts were discovered.
        if n == shape_size:
            break

    # Move the rock.
    new_map = np.copy(map_)
    new_map[new_map == "@"] = "."
    for j, i in indices:
        new_map[j, i] = "@"

    return new_map


def vertical_movement_possible(map_, shape_size):

    # Let n be the number of parts that were already checked.
    n = 0

    # Iterate over the map and check each part of the rock.
    for j in range(map_.shape[0]):
        for i in range(map_.shape[1]):

            # Check if a rock is at the current position.
            if map_[j, i] == "@":

                n += 1

                # Check if moving the rock would case any problems.
                try:
                    if map_[j+1, i] in [".", "@"]:
                        continue
                except IndexError:
                    pass

                return False

            # Check if all parts were discovered.
            if n == shape_size:
                return True

    return True


def move_vertically(map_, shape_size):

    # Let n be the number of parts that were already checked.
    n = 0

    # Iterate over the map and save coordinates of the rock parts.
    indices = []
    for j in range(map_.shape[0]):
        for i in range(map_.shape[1]):

            # Check if a rock is at the current position.
            if map_[j, i] == "@":

                n += 1

                # Save coordinates of the new rock part.
                indices.append((j+1, i))

            # Check if all parts were discovered.
            if n == shape_size:
                break
        # Check if all parts were discovered.
        if n == shape_size:
            break

    # Move the rock.
    new_map = np.copy(map_)
    new_map[new_map == "@"] = "."
    for j, i in indices:
        new_map[j, i] = "@"

    return new_map


def part_one(jet_pattern):

    # Initialize a map.
    map_ = np.zeros((1, 7), dtype=str)
    map_[:, :] = "."

    # Declare a variables to keep track of shapes
    # and jet pattern position.
    shape_ind, jet_ind = 0, 0

    # Simulate 2022 falling rocks.
    for _ in range(2022):

        # Add a rock to the map and save the shape size.
        map_, shape_size = add_shape(shape_ind, map_)

        # Simulate the rock falling.
        in_motion = True
        while in_motion:

            # Get horizontally direction and update position.
            direction = jet_pattern[jet_ind]
            direction = -1 if direction == "<" else 1
            jet_ind = (jet_ind + 1) % len(jet_pattern)

            # Simulate the gas.
            if horizontal_movement_possible(map_, direction, shape_size):
                map_ = move_horizontally(map_, direction, shape_size)

            # Simulate gravity.
            if vertical_movement_possible(map_, shape_size):
                map_ = move_vertically(map_, shape_size)
            else:
                break

        # Stop the rock.
        map_[map_ == "@"] = "#"

        # Update shape.
        shape_ind = (shape_ind + 1) % 5

    # Remove lines of air.
    while np.all(map_[0, :] == "."):
        map_ = np.delete(map_, 0, 0)

    return map_.shape[0]


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readline()

    # Solve part one.
    result1 = part_one(data)

    # Print the results for the day.
    print(f"Part One: {result1}")


if __name__ == "__main__":
    main()
