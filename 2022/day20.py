import copy as c


def mix(data, part_two):

    if part_two:
        # Apply decryption key from part two to each number.
        for i, _ in enumerate(data):
            data[i] *= 811589153

    # Create a list with IDs that corresponds to the
    # items within the data so that you exactly know which
    # item needs to be moved in case that there are duplicates.
    ids = list(range(len(data)))

    # Create copies of both arrays where you can change the order
    # while maintaining the initial order within the other arrays.
    new_data: list = c.copy(data)
    new_ids: list = c.copy(ids)

    # Iterate over the original lists.
    for _ in range(10 if part_two else 1):
        for item, id_ in zip(data, ids):

            # Get the current index of the item and calculate the new index.
            ind = new_ids.index(id_)
            new_ind = (ind+item) % (len(data)-1)

            # Check if the new index equals zero. This is necessary since the
            # insert()-function does not work like the exercise expects it in
            # this case.
            if new_ind != 0:
                # Remove item at current index and insert it at the new one.
                new_data.insert(new_ind, new_data.pop(ind))
                new_ids.insert(new_ind, new_ids.pop(ind))
            else:
                # Remove item at current index an append it
                # to the end of the list.
                new_data.append(new_data.pop(ind))
                new_ids.append(new_ids.pop(ind))

    # Get the index of the number zero.
    zero_ind = new_data.index(0)

    # Find the 1000th, 2000th and 3000th numbers after the value zero
    # with repeating the list.
    first = new_data[(1000 + zero_ind) % len(new_data)]
    second = new_data[(2000 + zero_ind) % len(new_data)]
    third = new_data[(3000 + zero_ind) % len(new_data)]

    return sum([first, second, third])


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [int(item.strip()) for item in data]

    # Solve part one.
    result1 = mix(data, part_two=False)

    # Solve part two.
    result2 = mix(data, part_two=True)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
