def part_one(data, values):

    # Store the duplicate items in the following array.
    duplicates = []

    # Iterate over the data.
    for rucksack in data:

        # Let l be the size of one component.
        comp_len = int(len(rucksack)/2)

        # Split rucksack into components.
        comp1 = rucksack[:comp_len]
        comp2 = rucksack[comp_len:]

        # Iterate over the first component and finde the
        # duplicate item.
        for item in comp1:
            if item in comp2:
                duplicates.append(item)
                break

    # Get the total sum of the values of the duplicate items.
    total_sum = 0
    for char in duplicates:
        total_sum += values.index(char) + 1

    return total_sum


def part_two(data, values):

    total_sum = 0

    # Iterate over the groups.
    for i in range(0, len(data), 3):

        # Get and transform group.
        group = data[i:i+3]
        group = [set(item) for item in group]

        # Get the item that all three backpacks have in common.
        item = group[0].intersection(group[1]).intersection(group[2])

        # Add item values to total sum.
        total_sum += values.index(list(item)[0]) + 1

    return total_sum


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Store the letters within an array where the indices
    # indicate the letters value.
    values = list(range(ord('a'), ord('z') + 1))
    values += list(range(ord('A'), ord('Z')+1))
    values = [chr(item) for item in values]

    # Solve part one.
    result1 = part_one(data, values)

    # Solve part two.
    result2 = part_two(data, values)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
