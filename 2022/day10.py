import numpy as np


def check_cycle(i, x, signal_strengths: list):

    # Check if cycle fulfills condition.
    if i in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(i * x)


def move_cursor(pos_x, pos_y):

    # Increment x and y positions based
    # on their values.
    if pos_x == 39:
        pos_x = 0
        pos_y += 1
    else:
        pos_x += 1

    return pos_x, pos_y


def change_sprite(x):

    # Change the sprite position based on x.
    new_sprite = np.array(list("........................................"))
    if x == -1:
        new_sprite[0] = "#"
    elif x == 0:
        new_sprite[:2] = "#"
    else:
        new_sprite[x-1:x+2] = "#"

    return ''.join(new_sprite)


def pretty_screen(screen):

    screen_str = ""

    for i in range(screen.shape[0]):
        screen_str += ''.join(screen[i])
        screen_str += "\n"

    return screen_str.replace(".", " ")


def part_one(data):

    # Execute the instructions step by step.
    i, x = 1, 1
    signal_strengths = []
    while True:

        if len(data) == 0:
            break

        # Get the current instruction.
        instr = data[0]

        # Check cycle condition.
        check_cycle(i, x, signal_strengths)

        # Check the instruction type.
        if instr[0] == "a":  # 'add'

            # Increase cycles and check for cycle condition.
            i += 1
            check_cycle(i, x, signal_strengths)
            i += 1

            # Increase x value after two cycles.
            x += int(instr.split(" ")[1])

        else:  # 'noop'
            i += 1

        # Remove the current instruction.
        data = data[1:]

    return sum(signal_strengths)


def part_two(data):

    # Initialize the blank screen.
    screen = np.zeros(((6, 40)), dtype=str)

    # Initialize sprite and screen positions.
    sprite = "###....................................."
    pos_x, pos_y = 0, 0
    x = 1

    # Execute the instructions.
    while True:

        # Break if all instructions have been executed.
        if len(data) == 0:
            break

        # Get the instruction.
        instr = data[0]

        # Check the type of instruction.
        if instr[0] == "a":

            # Draw on the screen twice.
            screen[pos_y, pos_x] = sprite[pos_x]
            pos_x, pos_y = move_cursor(pos_x, pos_y)
            screen[pos_y, pos_x] = sprite[pos_x]

            # Increment x and adjust the sprite.
            x += int(instr.split(" ")[1])
            sprite = change_sprite(x)

        else:
            # Draw on the screen.
            screen[pos_y, pos_x] = sprite[pos_x]

        # Increment x and y positions.
        pos_x, pos_y = move_cursor(pos_x, pos_y)

        # Remove the instruction after it is completed.
        data = data[1:]

    return "\n" + pretty_screen(screen)


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Solve part one.
    result1 = part_one(data)

    # Solve part two.
    result2 = part_two(data)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
