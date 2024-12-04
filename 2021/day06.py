import copy as c


def simulate_growth(fishes, days):

    for _ in range(days):

        new_fishes = c.copy(fishes)

        for i in [0, 1, 2, 3, 4, 5, 7]:
            new_fishes[i] = fishes[i+1]

        new_fishes[6] = fishes[7] + fishes[0]
        new_fishes[8] = fishes[0]

        fishes = c.copy(new_fishes)

    return sum(fishes.values())


def main():

    with open("input.txt") as f:
        data = f.read()
    data = [int(item) for item in data.split(",")]

    fishes = {}
    for i in range(0, 9):
        fishes[i] = data.count(i)

    print(f"Part One: {simulate_growth(fishes, 80)}")
    print(f"Part Two: {simulate_growth(fishes, 256)}")


if __name__ == "__main__":
    main()
