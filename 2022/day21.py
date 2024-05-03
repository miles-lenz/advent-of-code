import sympy as sp


def part_one(data):

    monkeys = {}
    monkeys_shouted = {}

    # Iterate over the monkeys.
    for monkey in data:
        monkey: str = monkey

        # Extract monkey information.
        name = monkey.split(": ")[0]
        operation = monkey.split(": ")[1]

        # Save information.
        monkeys[name] = operation
        if operation.isdigit():
            monkeys_shouted[name] = 1
        else:
            monkeys_shouted[name] = 0

    # Continue until the root monkey can shout his number.
    while not monkeys_shouted["root"]:

        # Iterate over all monkeys.
        for name, operation in monkeys.items():

            # Continue if monkey has already shouted.
            if monkeys_shouted[name]:
                continue

            # Get monkey names needed for operation and
            # the actual operator symbol.
            name1, operator, name2 = operation.split(" ")

            # Check if both other monkey have shouted their
            # number already.
            if monkeys_shouted[name1] and monkeys_shouted[name2]:

                # Calculate number.
                num = eval(monkeys[name1] + operator + monkeys[name2])

                # Save number and that the monkey shouted.
                monkeys[name] = str(num)
                monkeys_shouted[name] = 1

    return int(float(monkeys["root"]))


def part_two(data):

    monkeys = {}
    for monkey in data:

        # Extract information.
        name, operation = monkey.split(": ")

        # Check for myself.
        if name == "humn":
            operation = "x"

        # Save information.
        monkeys[name] = operation

    # Get both sides of the root equation.
    eq1, eq2 = monkeys["root"].split(" + ")

    # Replace variables until nothing in the
    # equation changes anymore.
    while True:

        # Replace operations within the equation.
        new_eq1, new_eq2 = eq1, eq2
        for name, operation in monkeys.items():
            if name in eq1:
                new_eq1 = new_eq1.replace(name, "(" + operation + ")")
            if name in eq2:
                new_eq2 = new_eq2.replace(name, "(" + operation + ")")

        # Break if nothing changes.
        if new_eq1 == eq1 and new_eq2 == eq2:
            break
        eq1, eq2 = new_eq1, new_eq2

    # Replace strings with actual sympy expressions.
    x = sp.symbols("x")
    eq1 = eval(eq1)
    eq2 = eval(eq2)

    # Solve the equation.
    return int(sp.solve(sp.Eq(eq1, eq2), x)[0])


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
