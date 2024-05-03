def adjacentToSymbol(i, j, size, data, possibleGears, numOnBorder):

    symbols = []
    for di in [i-1, i, i+1]:
        for dj in range(j-1, j+size+1):
            if di < 0 or dj < 0:
                continue
            try:
                item = data[di][dj]
                if not item.isdigit() and item != ".":
                    symbols.append(item)
                    if numOnBorder:
                        j += 1
                    num = int(data[i][j:j+size])
                    if f"{di}, {dj}" in possibleGears.keys():
                        possibleGears[f"{di}, {dj}"][0] += 1
                        possibleGears[f"{di}, {dj}"][1].append(num)
                    else:
                        possibleGears[f"{di}, {dj}"] = [1, [num]]

            except IndexError:
                pass

    return len(symbols) != 0


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    possibleGears = dict()

    sum_ = 0
    for i, line in enumerate(data):
        num = ""
        for j, char in enumerate(line):
            if char.isdigit():
                num += char
            if (not char.isdigit() or j == len(line) - 1) and len(num) > 0:
                if adjacentToSymbol(
                        i, j-len(num), len(num), data, possibleGears,
                        j == len(line) - 1 and char.isdigit()):
                    sum_ += int(num)
                num = ""

    print(f"Part One: {sum_}")

    sum_ = 0
    for key in possibleGears.keys():
        if possibleGears[key][0] != 2:
            continue
        else:
            sum_ += possibleGears[key][1][0] * possibleGears[key][1][1]

    print(f"Part Two: {sum_}")


if __name__ == "__main__":
    main()
