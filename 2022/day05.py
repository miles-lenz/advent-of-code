import numpy as np


def move_crates(data, reverse):

    # Separate the instructions from the crane information.
    instructions, crane_info = [], []
    for item in data:

        # Save crane information.
        if item != "" and "[" in item:
            crane_info.append(item)

        # Save instructions.
        elif item != "" and item[0] == "m":
            instructions.append(item)

        # Let n be the amount of cranes.
        elif item != "":
            n = int(item.strip()[-1])

    # Transform crane information.
    crane_info = np.array([list(item) for item in crane_info])

    # Extract the information about each crane.
    cranes = {}
    for i, ind in enumerate(range(1, 4*n, 4)):
        sub_info = crane_info[:, ind]
        cranes[i+1] = np.delete(sub_info, np.where(sub_info == " "))[::-1]

    # Iterate over the instructions.
    for instr in instructions:

        # Extract only useful information.
        amount, from_, to = np.array(instr.split(" "))[[1, 3, 5]].astype(int)

        # Move the crates according to the instructions.
        if reverse:
            cranes[to] = np.concatenate(
                (cranes[to], cranes[from_][-amount:][::-1]))
        else:
            cranes[to] = np.concatenate(
                (cranes[to], cranes[from_][-amount:]))
        cranes[from_] = cranes[from_][:-amount]

    # Find the crates on top of each stack.
    top_crates = ""
    for _, stack in cranes.items():
        top_crates += stack[-1]

    return top_crates


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.replace("\n", "") for item in data]

    # Solve part one.
    result1 = move_crates(data, True)

    # Solve part two.
    result2 = move_crates(data, False)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
