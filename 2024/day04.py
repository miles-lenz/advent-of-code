import re
import numpy as np


def main():

    with open("input.txt") as f:
        data = f.readlines()

    data = [list(item.strip()) for item in data]
    data = np.array(data)

    pattern = r"(?=(XMAS|SAMX))"

    count1 = 0
    for i in range(data.shape[0]):

        row = "".join(data[i, :])
        col = "".join(data[:, i])

        count1 += len(re.findall(pattern, row))
        count1 += len(re.findall(pattern, col))

    data_rot = np.rot90(data)
    for i in range(-data.shape[0], data.shape[0]):
        diagonal = "".join(data.diagonal(i))
        diagonal += " " + "".join(data_rot.diagonal(i))
        count1 += len(re.findall(pattern, diagonal))

    count2 = 0
    for i in range(data.shape[0] - 2):
        for j in range(data.shape[1] - 2):

            sub_data = data[i:i + 3, j:j + 3]
            x1 = "".join(sub_data.diagonal())
            x2 = "".join(np.rot90(sub_data).diagonal())

            valid = ["MAS", "SAM"]
            if x1 in valid and x2 in valid:
                count2 += 1

    print(f"Part One: {count1}")
    print(f"Part Two: {count2}")


if __name__ == "__main__":
    main()
