import numpy as np


def part_one(data):

    visible = 0

    # Iterate over the grid.
    for j in range(1, data.shape[0]-1):
        for i in range(1, data.shape[1]-1):

            current_tree = data[j, i]

            # Get tree lines with respect to the current tree.
            top, bottom = data[:j, i], data[j+1:, i]
            left, right = data[j, :i], data[j, i+1:]

            # Create boolean arrays that indicate if a tree in
            # the tree line is shorter than the current tree.
            top_comp = [x < current_tree for x in top]
            bottom_comp = [x < current_tree for x in bottom]
            left_comp = [x < current_tree for x in left]
            right_comp = [x < current_tree for x in right]

            # Check if at least one tree line contains only shorter trees.
            for comp in [top_comp, bottom_comp, left_comp, right_comp]:
                if np.all(comp):
                    visible += 1
                    break

    # Add edge tree to the visible count.
    visible += data.shape[0]*2 + (data.shape[1]-2)*2

    return visible


def part_two(data):

    scenic_scores = []

    # Iterate over the grid.
    for j in range(data.shape[0]):
        for i in range(data.shape[1]):

            current_tree = data[j, i]

            # Store the distances in an array of the
            # form [top(0), bottom(1), left(2), right(3)].
            distances = np.empty(4)

            # Get all tree lines.
            top, bottom = data[:j, i][::-1], data[j+1:, i]
            left, right = data[j, :i][::-1], data[j, i+1:]

            # Iterate over the different tree lines.
            for k, line in enumerate([top, bottom, left, right]):

                if len(line) == 0:  # Check for edge trees.
                    distances[k] = 0
                else:
                    # Check if all trees in the line are shorter.
                    if np.all([x < current_tree for x in line]):
                        distances[k] = len(line)
                    else:
                        # Get the length of the view.
                        length = np.argmax(line >= current_tree)
                        distances[k] = length + 1

            # Calculate and save the scenic score.
            score = distances[0] * distances[1] * distances[2] * distances[3]
            scenic_scores.append(int(score))

    return max(scenic_scores)


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Transform data.
    data = [list(item) for item in data]
    data = np.array(data, dtype=int)

    # Solve part one.
    result1 = part_one(data)

    # Solve part two.
    result2 = part_two(data)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
