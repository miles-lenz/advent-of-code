def get_amount(data, distinct_chars):

    # Iterate over the data.
    marker, amount_chars = data[:distinct_chars], distinct_chars
    for char in data[distinct_chars:]:

        # Break if the marker contains only unique values.
        if len(set(marker)) == distinct_chars:
            break

        # Adjust the marker and increase the character amount.
        marker = marker[1:] + [char]
        amount_chars += 1

    return amount_chars


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Transform data into list of characters.
    data = list(data[0])

    # Solve part one.
    result1 = get_amount(data, 4)

    # Solve part two.
    result2 = get_amount(data, 14)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
