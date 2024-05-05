# WARNING: This implementation is rather slow (1-2 minutes) and inefficient.

def calculate_min_fuel(data, constant_rate):

    min_fuel = float('inf')
    for i in range(max(data) + 1):

        fuel = 0
        for crab in data:

            if constant_rate:
                fuel += abs(i - crab)
            else:
                dist = abs(i - crab)
                fuel += sum([j for j in range(1, dist + 1)])

        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


def main():

    with open("input.txt") as f:
        data = f.read()
    data = [int(item) for item in data.split(",")]

    print(f"Part One: {calculate_min_fuel(data, True)}")
    print(f"Part Two: {calculate_min_fuel(data, False)}")


if __name__ == "__main__":
    main()
