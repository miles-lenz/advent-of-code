import numpy as np


def get_sub_dir(top_dir, path):

    # Find the sub directory specified by the path.
    sub_dir = top_dir
    for key in path:
        sub_dir = sub_dir[key]

    return sub_dir


def compute_dir_size(dir_: dict, sizes: list):

    # Check if all sub directories have the size already computed.
    for value in dir_.values():

        if isinstance(value, dict):
            if "size" not in value.keys():
                compute_dir_size(value, sizes)

    # Compute the directory size.
    size = 0
    for value in dir_.values():

        # Check the value type.
        if isinstance(value, dict):
            size += value["size"]
        else:
            size += int(value)

    # Add the directory size to the directory and the size list.
    if list(dir_.keys()) != ["/"]:
        dir_["size"] = size
        sizes.append(size)


def part_one(data):

    # Create a dictionary which represents the top level directory.
    # In addition, create the start path.
    top_dir, path = {"/": {}}, ["/"]

    # Iterate over the data.
    for line in data:

        # Check if line equals a command.
        if line[0] == "$":

            # Execute the command.
            if "cd .." in line:
                path = path[:-1]
            elif "cd /" in line:
                path = ["/"]
            elif "cd" in line:
                path += [line.split(" ")[-1]]

        # If line is no command it has to be a list item.
        else:

            # Check if list item is a directory.

            if "dir" in line:
                new_dir = line.split(" ")[1]
                get_sub_dir(top_dir, path)[new_dir] = {}
            else:
                size, name = line.split(" ")
                get_sub_dir(top_dir, path)[name] = size

    # Create a list to store all sizes.
    sizes = []

    # Compute the size of all directories.
    compute_dir_size(top_dir, sizes)

    # Sum up all sizes that with size at most 100000.
    sizes = np.array(sizes)

    return np.sum(sizes[sizes <= 100000]), top_dir, sizes


def part_two(dir_, sizes):

    # Compute the necessary space information.
    total_space = 70000000
    unused_space = total_space - dir_["/"]["size"]
    needed_space = 30000000 - unused_space

    # Iterate over the sizes and find the differences with respect
    # to the needed space.
    differences = np.empty(len(sizes))
    for i, size in enumerate(sizes):
        differences[i] = (size - needed_space)

    # Replace all negative entries with infinity.
    differences[differences < 0] = np.inf

    # Find the closest size that will free up enough space.
    return sizes[np.argmin(differences)]


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Solve part one.
    result1, dir_, sizes = part_one(data)

    # Solve part two.
    result2 = part_two(dir_, sizes)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
