def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()

    # Transform data.
    data = [item.strip() for item in data]
    data.append('')  # This is needed for the iteration to work correctly.

    # Initialize some variables.
    sums = [0] * (data.count('') + 1)
    temp_sum = 0
    i = 0

    # Iterate over the data.
    for item in data:

        # Check wether the data contains anything:
        if item == '':
            # Save the calories of one elf.
            sums[i] = temp_sum
            temp_sum, i = 0, i+1
        else:
            # Add item to temporary sum.
            temp_sum += int(item)

    # Get the maximum amount of calories.
    result1 = max(sums)

    # Get the amount of calories of the top three elves.
    result2 = sum(sorted(sums)[-3:])

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
