import copy as c


def compare(packet1, packet2):

    # Check for empty lists.
    if len(packet1) == 0 and len(packet2) != 0:
        return True
    if len(packet2) == 0 and len(packet1) != 0:
        return False

    # Iterate over packets.
    for i in range(max([len(packet1), len(packet2)])):

        # Get the items.
        try:
            item1 = packet1[i]
        except IndexError:
            return True
        try:
            item2 = packet2[i]
        except IndexError:
            return False

        # Check if both items are integers.
        if isinstance(item1, int) and isinstance(item2, int):

            # Compare the integers.
            if item1 < item2:
                return True
            if item2 < item1:
                return False
            continue

        # Check that both items are list.
        if isinstance(item1, int) and isinstance(item2, list):
            item1 = [item1]
        if isinstance(item1, list) and isinstance(item2, int):
            item2 = [item2]

        # Compare both list items.
        compared = compare(item1, item2)
        if compared is not None:
            return compared

    return None


def check_order(sorted_):

    # Iterate over the sorted list in pairs.
    for i in range(len(sorted_)-1):

        # Check if the order is correct.
        if not compare(sorted_[i], sorted_[i+1]):
            return False

    return True


def part_one(data):

    # Store number of correctly ordered pairs
    correct = []

    # Iterate over the data.
    for k, i in enumerate(range(0, len(data), 3)):

        # Get the packets.
        packet1 = eval(data[i])
        packet2 = eval(data[i+1])

        # Check if order is correct and append to the list.
        compared = compare(packet1, packet2)
        if compared:
            correct.append(k+1)

    # Compute the result.
    return sum(correct)


def part_two(data):

    # Remove blank lines and evaluate the items.
    data = [eval(item) for item in data if item != ""]

    # Add the divider packets.
    data.append([[2]])
    data.append([[6]])

    # Sort the data so that all packets are in the correct order.
    sorted_ = [data.pop(0)]

    while len(data) != 0:

        # Get new packet from data.
        packet = data.pop(0)

        # Test all different positions for new packet.
        for i in range(len(sorted_)+1):

            # Insert new packet.
            new_sorted = c.copy(sorted_)
            new_sorted.insert(i, packet)

            # Check the order.
            if check_order(new_sorted):
                sorted_ = c.copy(new_sorted)
                break

    # Get indices of divider packets.
    ind1 = sorted_.index([[2]]) + 1
    ind2 = sorted_.index([[6]]) + 1

    return ind1 * ind2


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Solve part one.
    result1 = part_one(c.copy(data))

    # Solve part two.
    result2 = part_two(c.copy(data))

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == main():
    main()
