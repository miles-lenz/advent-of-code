def formatData(data):

    data = [item.strip() for item in data]
    for i, game in enumerate(data):
        list_ = []
        for round_ in game.split(": ")[1].split("; "):
            dict_ = dict()
            for num, col in [item.split(" ") for item in round_.split(", ")]:
                dict_[col] = int(num)
            list_.append(dict_)
        data[i] = list_

    return data


def calculateSum(data, partTwo):

    if not partTwo:
        availableCubes = {
            "red": 12,
            "green": 13,
            "blue": 14
        }

    sum_ = 0
    for i, game in enumerate(data):

        if not partTwo:
            gameImpossible = False
        else:
            maxVals = {
                "red": -float("inf"),
                "green": -float("inf"),
                "blue": -float("inf")
            }

        for round_ in game:
            for col in round_.keys():
                if not partTwo:
                    if round_[col] > availableCubes[col]:
                        gameImpossible = True
                        break
                else:
                    if round_[col] > maxVals[col]:
                        maxVals[col] = round_[col]
            if not partTwo and gameImpossible:
                break

        if not partTwo and not gameImpossible:
            sum_ += i + 1

        if partTwo:
            maxVals = list(maxVals.values())
            sum_ += maxVals[0] * maxVals[1] * maxVals[2]

    return sum_


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = formatData(data)

    print(f"Part One: {calculateSum(data, False)}")
    print(f"Part Two: {calculateSum(data, True)}")


if __name__ == "__main__":
    main()
