def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    result1 = 0
    result2 = 0

    # Iterate over the data.
    for pair in data:

        # Split the pair.
        elf1, elf2 = pair.split(",")

        # Transform the assignments.
        elf1, elf2 = elf1.split("-"), elf2.split("-")
        elf1, elf2 = [int(x) for x in elf1], [int(x) for x in elf2]

        # Check if one assignment covers the other one completely.
        if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
            result1 += 1
        elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
            result1 += 1

        elf1 = set(range(elf1[0], elf1[1] + 1))
        elf2 = set(range(elf2[0], elf2[1] + 1))

        # Check if one assignment covers the other one by at least one slot.
        if len(elf1.intersection(elf2)) > 0:
            result2 += 1

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
