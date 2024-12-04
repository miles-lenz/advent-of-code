import numpy as np


def extract_monkey_information(data):

    monkeys = {}

    # Iterate over the data.
    for item in data:

        # Get information based on keywords.
        if "Monkey" in item:

            # Create a new monkey profile.
            id_ = int(item.split(" ")[1][:-1])
            monkeys[id_] = {}

        elif "Starting" in item:

            # Save items the monkey is holding.
            items = item.split(": ")[1].split(", ")
            items = [int(num) for num in items]
            monkeys[id_]["items"] = items

        elif "Operation" in item:
            monkeys[id_]["op"] = item.split("= ")[1]

        elif "Test" in item:
            monkeys[id_]["test"] = int(item.split(" ")[-1])

        elif "true" in item:
            monkeys[id_]["true"] = int(item.split(" ")[-1])

        elif "false" in item:
            monkeys[id_]["false"] = int(item.split(" ")[-1])

        elif item == "":
            continue

        else:
            raise Exception(f"An item could not be matched: {item}")

    return monkeys


def part_one(data):

    # Save all information about monkeys in a dictionary.
    monkeys = extract_monkey_information(data)
    amount_monkeys = max(monkeys.keys()) + 1

    # Create an array to store how many items each monkey inspected.
    inspections = [0 for _ in range(amount_monkeys)]

    # Simulate 20 rounds.
    for _ in range(20):

        # Iterate over the monkeys.
        for i in range(amount_monkeys):

            # Iterate over the items the monkey holds.
            for item in monkeys[i]["items"]:

                # Increment the amount of inspections for that monkey.
                inspections[i] += 1

                # Execute the operation.
                item = eval(monkeys[i]["op"].replace("old", str(item)))

                # Decrease the worry level.
                item = int(item / 3)

                # Execute the test.
                if item % monkeys[i]["test"] == 0:
                    monkeys[monkeys[i]["true"]]["items"].append(item)
                else:
                    monkeys[monkeys[i]["false"]]["items"].append(item)

            # Remove the items from the current monkey.
            monkeys[i]["items"] = []

    # Sort the amount of inspections.
    inspections = sorted(inspections)[::-1]

    return inspections[0] * inspections[1]


def part_two(data):

    # Save all information about monkeys in a dictionary.
    monkeys = extract_monkey_information(data)
    amount_monkeys = max(monkeys.keys()) + 1

    # Create an array to store how many items each monkey inspected.
    inspections = [0 for _ in range(amount_monkeys)]

    # Find the greatest common divisor for the 'divisible by' numbers.
    # Once an item passes this number you can simply replace it with
    # 'item % gcd' since it will have the same behavior as the original
    # number. This is only the case for numbers that are
    # mutually prime (teilerfremd).
    gcd = [monkeys[i]["test"] for i in range(amount_monkeys)]
    gcd = np.prod(gcd)

    # Simulate 10000 rounds.
    for _ in range(10000):

        # Iterate over the monkeys.
        for i in range(amount_monkeys):

            # Iterate over the items the monkey holds.
            for item in monkeys[i]["items"]:

                # Increment the amount of inspections for that monkey.
                inspections[i] += 1

                # Execute the operation.
                item = eval(monkeys[i]["op"].replace("old", str(item)))

                # Reduce item size without changing division behavior by using
                # the greatest common divisor.
                item = item % gcd

                # Execute the test.
                if item % monkeys[i]["test"] == 0:
                    monkeys[monkeys[i]["true"]]["items"].append(item)
                else:
                    monkeys[monkeys[i]["false"]]["items"].append(item)

            # Remove the items from the current monkey.
            monkeys[i]["items"] = []

    # Sort the amount of inspections.
    inspections = sorted(inspections)[::-1]

    return inspections[0] * inspections[1]


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Solve part one.
    result1 = part_one(data)

    # Solve part two.
    result2 = part_two(data)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
