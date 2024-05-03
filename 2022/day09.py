import copy as c


def is_moving_necessary(head_pos, tail_pos):

    # Extract x and y information.
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos

    # Check distance of head and tail and determine
    # wether moving is necessary.
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return False
    return True


def move_tail(head_pos, tail_pos):

    new_tail_pos = c.copy(tail_pos)

    # Extract x and y information.
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos

    # Check for horizontal alignment.
    if head_x == tail_x:
        new_tail_pos[1] += 1 if head_y > tail_y else -1

    # Check for vertical alignment.
    elif head_y == tail_y:
        new_tail_pos[0] += 1 if head_x > tail_x else -1

    # Check for diagonal alignment.
    else:
        new_tail_pos[1] += 1 if head_y > tail_y else -1
        new_tail_pos[0] += 1 if head_x > tail_x else -1

    return new_tail_pos


def move_middle_parts(head_pos, middle_pos):

    for i in range(8):

        if i == 0:
            needs_moving = is_moving_necessary(head_pos, middle_pos[i])
            if needs_moving:
                middle_pos[i] = move_tail(head_pos, middle_pos[i])
        else:
            needs_moving = is_moving_necessary(middle_pos[i-1], middle_pos[i])
            if needs_moving:
                middle_pos[i] = move_tail(middle_pos[i-1], middle_pos[i])

    return middle_pos


def simulate_rope(data, middle_parts):

    # Initialize starting positions => [x, y]
    head_pos = [0, 0]
    tail_pos = [0, 0]
    if middle_parts:
        middle_pos = {}
        for i in range(8):
            middle_pos[i] = [0, 0]

    # Save visited spots of the tail.
    visited = ["0,0"]

    # Iterate over the data.
    for instruction in data:

        direction, length = instruction.split(" ")

        # Figure out direction.
        if direction == "R":
            ind, sign = 0, 1
        elif direction == "L":
            ind, sign = 0, -1
        elif direction == "U":
            ind, sign = 1, 1
        else:  # direction == "D"
            ind, sign = 1, -1

        # Move step by step.
        for _ in range(int(length)):

            # Move the head.
            head_pos[ind] += sign

            # Move the middle parts.
            if middle_parts:
                middle_pos = move_middle_parts(head_pos, middle_pos)

            # Check if tail needs to be moved.
            if not middle_parts:
                needs_moving = is_moving_necessary(head_pos, tail_pos)
            else:
                needs_moving = is_moving_necessary(middle_pos[7], tail_pos)

            # Need tail if necessary.
            if needs_moving:
                if not middle_parts:
                    tail_pos = move_tail(head_pos, tail_pos)
                else:
                    tail_pos = move_tail(middle_pos[7], tail_pos)

            # Save tail position if it wasn't already visited.
            tail_pos_str = f"{tail_pos[0]},{tail_pos[1]}"
            if tail_pos_str not in visited:
                visited.append(tail_pos_str)

    return len(visited)


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Solve part one.
    result1 = simulate_rope(data, False)

    # Solve part two.
    result2 = simulate_rope(data, True)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
