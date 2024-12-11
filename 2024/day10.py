import numpy as np


def main():

    with open("input.txt") as f:
        data = [list(item.strip()) for item in f.readlines()]
    data = np.array(data, dtype=int)

    sum_scores, sum_ratings = 0, 0
    for index_zero in np.argwhere(data == 0):

        score, rating = 0, 0
        visited_tops = []

        queue = [index_zero]
        while queue != []:

            row, col = queue.pop(0)

            if data[row, col] == 9:
                rating += 1
                if [row, col] not in visited_tops:
                    score += 1
                    visited_tops.append([row, col])
                continue

            shape, target = data.shape, data[row, col] + 1

            if row + 1 < shape[0] and data[row + 1, col] == target:
                queue.append((row + 1, col))
            if row - 1 >= 0 and data[row - 1, col] == target:
                queue.append((row - 1, col))
            if col + 1 < shape[1] and data[row, col + 1] == target:
                queue.append((row, col + 1))
            if col - 1 >= 0 and data[row, col - 1] == target:
                queue.append((row, col - 1))

        sum_scores += score
        sum_ratings += rating

    print(f"Part One: {sum_scores}")
    print(f"Part Two: {sum_ratings}")


if __name__ == "__main__":
    main()
