import numpy as np


def calculate_overlapping_points(lines, diagram, include_diagonal):

    for start, end in lines:

        x_vals, y_vals = [start[0], end[0]], [start[1], end[1]]

        if x_vals[0] == x_vals[1]:
            y_range = list(range(*np.sort(y_vals)))
            y_range.append(y_range[-1] + 1)
            diagram[y_range, x_vals[0]] += 1
        elif y_vals[0] == y_vals[1]:
            x_range = list(range(*np.sort(x_vals)))
            x_range.append(x_range[-1] + 1)
            diagram[y_vals[0], x_range] += 1
        elif include_diagonal:
            x_step = 1 if x_vals[0] < x_vals[1] else -1
            x_range = list(range(*x_vals, x_step))
            x_range.append(x_range[-1] + x_step)
            y_step = 1 if y_vals[0] < y_vals[1] else -1
            y_range = list(range(*y_vals, y_step))
            y_range.append(y_range[-1] + y_step)
            diagram[y_range, x_range] += 1

    return len(np.where(diagram >= 2)[0])


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    lines = []
    max_x, max_y = 0, 0

    for line in data:

        start, end = line.split(" -> ")
        start = [int(item) for item in start.split(",")]
        end = [int(item) for item in end.split(",")]

        lines.append([start, end])

        if start[0] > max_x or end[0] > max_x:
            max_x = np.max([start[0], end[0]])
        if start[1] > max_y or end[1] > max_y:
            max_y = np.max([start[1], end[1]])

    diagram = np.zeros((max_y + 1, max_x + 1))

    part_one = calculate_overlapping_points(lines, np.copy(diagram), False)
    part_two = calculate_overlapping_points(lines, np.copy(diagram), True)

    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
