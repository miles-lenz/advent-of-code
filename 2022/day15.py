def extract(data):

    # Save sensor and beacons coordinates.
    sensors, beacons = [], []

    for line in data:

        # Extract sensor and closest beacon.
        sensor, beacon = line.split(": ")

        # Remove unnecessary text and extract coordinates.
        sensor_x = int(sensor.split("x=")[1].split(",")[0])
        sensor_y = int(sensor.split("y=")[1])
        beacon_x = int(beacon.split("x=")[1].split(",")[0])
        beacon_y = int(beacon.split("y=")[1])

        # Store coordinates.
        sensors.append([sensor_y, sensor_x])
        beacons.append([beacon_y, beacon_x])

    return sensors, beacons


def part_one(sensors, beacons):

    # Initialize the height of the y line.
    y = 2000000

    # Save positions that are covered and where sensors/beacons are.
    pos_covered = []
    pos_obstacle = []

    # Iterate over sensor-beacon pairs.
    for sensor, beacon in zip(sensors, beacons):

        # Check if sensor or beacon is on the line.
        if sensor[0] == y and sensor not in pos_obstacle:
            pos_obstacle.append(sensor)
        elif beacon[0] == y and beacon not in pos_obstacle:
            pos_obstacle.append(beacon)

        # Compute Manhattan distance.
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        # Compute distance that is 'left' after moving to the y line.
        leftover = abs(sensor[0] - y)

        # Check if sensor could reach the y line.
        if leftover <= dist:

            # Subtract the distance that is needed in order to
            # get to the y line.
            dist -= leftover

            # Save the range the sensor can cover.
            pos_covered += list(range(sensor[1]-dist, sensor[1]+dist+1))

    return len(set(pos_covered)) - len(pos_obstacle)


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Extract useful information.
    sensors, beacons = extract(data)

    # Solve part one.
    result1 = part_one(sensors, beacons)

    # Print the results for the day.
    print(f"Part One: {result1}")


if __name__ == "__main__":
    main()
