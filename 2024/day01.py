import numpy as np


def main():

    with open("input.txt") as f:
        data = f.readlines()

    data = [item.strip().split("   ") for item in data]
    data = np.array(data, dtype=int)

    left = np.sort(data[:, 0])
    right = np.sort(data[:, 1])

    uniques, counts = np.unique(right, return_counts=True)
    counts = dict(zip(uniques, counts))

    sum_, sim_score = 0, 0
    for i in range(len(data)):
        sum_ += np.abs(left[i] - right[i])
        sim_score += 0 if left[i] not in uniques else left[i] * counts[left[i]]

    print(f"Part One: {sum_}")
    print(f"Part Two: {sim_score}")


if __name__ == "__main__":
    main()
