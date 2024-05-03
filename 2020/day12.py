def part_one(content):
    """Calculate the Manhattan distance."""

    directions = ["east", "south", "west", "north"]
    directionsIndex = 0
    position = {"north": 0, "east": 0}

    for instruction in content:

        if instruction[0] == "N":
            position["north"] += int(instruction[1:])
        elif instruction[0] == "S":
            position["north"] -= int(instruction[1:])
        elif instruction[0] == "E":
            position["east"] += int(instruction[1:])
        elif instruction[0] == "W":
            position["east"] -= int(instruction[1:])

        elif instruction[0] == "L":
            value = int(instruction[1:])
            if value == 90:
                directionsIndex -= 1
            elif value == 180:
                directionsIndex -= 2
            elif value == 270:
                directionsIndex -= 3

        elif instruction[0] == "R":
            value = int(instruction[1:])
            if value == 90:
                directionsIndex += 1
            elif value == 180:
                directionsIndex += 2
            elif value == 270:
                directionsIndex += 3

        elif instruction[0] == "F":
            if directionsIndex >= 0:
                index = directionsIndex % 4
            else:
                index = directionsIndex % -4
            facing = directions[index]

            if facing == "north":
                position["north"] += int(instruction[1:])
            elif facing == "east":
                position["east"] += int(instruction[1:])
            elif facing == "south":
                position["north"] -= int(instruction[1:])
            elif facing == "west":
                position["east"] -= int(instruction[1:])

    result = abs(position["north"]) + abs(position["east"])

    return result


def part_two(content):
    """Calculate distance between that location and starting position."""

    waypoint = [1, 10]
    ship_pos = [0, 0]

    for instruction in content:
        op, value = instruction[0], int(instruction[1:])

        if op == "N":
            waypoint[0] += value
        elif op == "S":
            waypoint[0] -= value
        elif op == "E":
            waypoint[1] += value
        elif op == "W":
            waypoint[1] -= value

        elif op == "L":
            if value == 90:
                waypoint = [waypoint[1]] + [-waypoint[0]]
            elif value == 180:
                waypoint = [-x for x in waypoint]
            elif value == 270:
                waypoint = [-waypoint[1]] + [waypoint[0]]
        elif op == "R":
            if value == 90:
                waypoint = [-waypoint[1]] + [waypoint[0]]
            elif value == 180:
                waypoint = [-x for x in waypoint]
            elif value == 270:
                waypoint = [waypoint[1]] + [-waypoint[0]]

        elif op == "F":
            ship_pos[0] += waypoint[0] * value
            ship_pos[1] += waypoint[1] * value

    result = abs(ship_pos[0]) + abs(ship_pos[1])

    return result


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [item.strip() for item in content]

    res1 = part_one(content)
    print(f'Part One: {res1}')

    res2 = part_two(content)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
