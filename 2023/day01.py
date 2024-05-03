def calculateSum(data, digits, partTwo):

    sum_ = 0
    for line in data:

        num = ""
        for i, list_ in enumerate([line, line[::-1]]):
            for j, char in enumerate(list_):

                if char.isdigit():
                    num += char
                    break

                if partTwo:
                    for digitStr, digitInt in digits:
                        try:
                            digitStr = digitStr[::-1] if i == 1 else digitStr
                            if (list_[j:].index(digitStr) == 0):
                                num += digitInt
                                break
                        except ValueError:
                            pass

                if len(num) == 1 and i == 0 or len(num) == 2 and i == 1:
                    break

        sum_ += int(num)

    return sum_


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    digits = [
        ("one", "1"), ("two", "2"), ("three", "3"),
        ("four", "4"), ("five", "5"), ("six", "6"),
        ("seven", "7"), ("eight", "8"), ("nine", "9")
    ]

    print(f"Part One: {calculateSum(data, digits, False)}")
    print(f"Part Two: {calculateSum(data, digits, True)}")


if __name__ == "__main__":
    main()
