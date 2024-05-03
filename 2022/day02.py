def get_result(player1, player2):

    if player1 == player2:
        return 3
    if player1 == "A":
        return 0 if player2 == "C" else 6
    if player1 == "B":
        return 0 if player2 == "A" else 6
    if player1 == "C":
        return 0 if player2 == "B" else 6


def part_one(data, vals):

    # Transform data.
    data = [item.replace("X", "A") for item in data]
    data = [item.replace("Y", "B") for item in data]
    data = [item.replace("Z", "C") for item in data]
    data = [item.split(" ") for item in data]

    # Iterate over the data.
    total_score = 0
    for opponent, you in data:
        total_score += vals[you] + get_result(opponent, you)

    return total_score


def part_two(data, vals):

    # Transform the data.
    data = [item.split(" ") for item in data]

    # Create a dictionary decision rules.
    decisions = {
        "A": {
            "X": "C",
            "Y": "A",
            "Z": "B",
        },
        "B": {
            "X": "A",
            "Y": "B",
            "Z": "C",
        },
        "C": {
            "X": "B",
            "Y": "C",
            "Z": "A",
        }
    }

    # Iterate over the data.
    total_score = 0
    for opponent, outcome in data:
        you = decisions[opponent][outcome]
        total_score += vals[you] + get_result(opponent, you)

    return total_score


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Define values for hand shapes.
    vals = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    # Solve part one.
    result1 = part_one(data, vals)

    # Solve part two.
    result2 = part_two(data, vals)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
