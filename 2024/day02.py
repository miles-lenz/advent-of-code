import numpy as np


def is_safe(line):

    diff = np.diff(np.array(line, dtype=int))

    if not (all(diff > 0) or all(diff < 0)):
        return False

    diff = np.abs(diff)
    if any(diff > 3):
        return False

    return True


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip().split(" ") for item in data]

    safe1, safe2 = 0, 0
    for line in data:

        if is_safe(line):
            safe1 += 1

        for i in range(len(line)):
            modified_line = np.delete(line, i)
            if is_safe(modified_line):
                safe2 += 1
                break

    print(f"Part One: {safe1}")
    print(f"Part Two: {safe2}")


if __name__ == "__main__":
    main()
