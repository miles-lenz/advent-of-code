import numpy as np


def snafu_to_decimal(num):

    decimal = 0

    # Convert SNAFU number into decimal number.
    for i, char in enumerate(num[::-1]):

        # Check for negative characters and convert the character
        # into an integer.
        if char == "-":
            char = -1
        elif char == "=":
            char = -2
        else:
            char = int(char)

        # Add the current characters value to the full number.
        decimal += char * 5**i

    return decimal


def decimal_to_snafu(num):

    # Calculate the needed length of the SNAFU number.
    length = 1
    while True:
        max_ = sum([2 * 5**i for i in range(length)])
        if -max_ <= num <= max_:
            break
        length += 1

    snafu = ""

    # Compute every SNAFU digit.
    for pos in range(length)[::-1]:

        # Get all possible values for this position.
        vals = np.array([-2, -1, 0, 1, 2], dtype=np.int64)
        vals *= 5**pos

        # Choose value that is closest to the number.
        closest = np.argmin(np.abs(num - vals)) - 2

        # Update leftover number.
        num -= closest * 5**pos

        # Convert closest number into actual SNAFU symbol.
        if closest == -2:
            closest = "="
        elif closest == -1:
            closest = "-"
        else:
            closest = str(closest)

        # Store symbol.
        snafu += closest

    return snafu


def part_one(numbers):

    sum_ = 0

    # Convert every number to decimal and sum them up.
    for num in numbers:
        sum_ += snafu_to_decimal(num)

    # Convert the sum into a SNAFU number.
    snafu = decimal_to_snafu(sum_)

    return snafu


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Solve part one.
    result1 = part_one(data)

    # Print the results for the day.
    print(f"Part One: {result1}")


if __name__ == "__main__":
    main()
