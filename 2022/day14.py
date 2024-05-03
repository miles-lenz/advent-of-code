import numpy as np


def create_cave(data):

    # Initialize max values for x and y.
    max_y, max_x = 0, 0

    # Iterate over the paths.
    for path in data:

        # Iterate over coordinates in path.
        for coordinates in path.split(" -> "):

            # Extract the coordinate x and y values.
            x, y = coordinates.split(",")
            x, y = int(x), int(y)

            # Check if any value is bigger than the currently
            # biggest one.
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    # Create an initial cave.
    # Remark: I guess you could make the cave size more memory efficient if you
    # were to dynamically add space if you need it. It just roughly calculated
    # how big it could get if there were to be no rocks and this worked.
    # Just guessing would have worked too.
    cave = np.zeros((max_y+5, max_x+2*max_y-1), dtype=str)
    cave[:, :] = "."

    # Iterate over the rock paths.
    for path in data:

        # Transform the path.
        path: str = path.split(" -> ")

        # Iterate over pairs of coordinates.
        for i in range(len(path)-1):

            # Get concrete coordinates.
            x1, y1 = path[i].split(",")
            x2, y2 = path[i+1].split(",")
            x1, y1 = int(x1), int(y1)
            x2, y2 = int(x2), int(y2)

            # Switch x and y coordinates in order to
            # guarantee that indexing will work.
            if x2 < x1:
                x1, x2 = x2, x1
            if y2 < y1:
                y1, y2 = y2, y1

            # Add rock path to cave.
            cave[y1:y2+1, x1:x2+1] = "#"

    return cave, max_y


def simulate_sand(cave, max_y, part_two):

    sand_x, sand_y = 500, 0

    i = 0
    while True:

        if not part_two:
            # Check if sand is below biggest rock y value.
            if sand_y > max_y:
                break

        # Check if cell below sand is free.
        if cave[sand_y + 1, sand_x] == ".":
            sand_y += 1
            continue

        # Check if below left cell is free.
        if cave[sand_y + 1, sand_x - 1] == ".":
            sand_x -= 1
            sand_y += 1
            continue

        # Check if below right cell is free.
        if cave[sand_y + 1, sand_x + 1] == ".":
            sand_x += 1
            sand_y += 1
            continue

        # Sand stays put.
        cave[sand_y, sand_x] = "o"

        # Break if the unit comes to rest at coordinates (500, 0).
        if part_two:
            if sand_y == 0 and sand_x == 500:
                break

        # Generate new sand and increment counter.
        sand_x, sand_y = 500, 0
        i += 1

    return i


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Create the cave based on the input.
    cave, max_y = create_cave(data)

    # Simulate the falling sand and solve part one.
    result1 = simulate_sand(np.copy(cave), max_y, False)

    # Change cave due to part two.
    cave[max_y+2, :] = "#"

    # Solve part two.
    result2 = simulate_sand(np.copy(cave), max_y, True) + 1

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
