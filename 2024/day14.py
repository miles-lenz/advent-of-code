import numpy as np
from PIL import Image


PATH = "2024/images/"


def store_img(robots, height, width, time):

    space = np.zeros((height, width), dtype="uint8")
    for pos, _ in robots:
        space[pos[1], pos[0]] = 255

    ratios = []

    h, w = height // 5, width // 5
    for row in range(0, height, h):
        for col in range(0, width, w):
            q = space[row:row+h, col:col+w]
            _, counts = np.unique(q, return_counts=True)
            ratio = counts[0] / counts[1] if len(counts) != 1 else 0
            ratios.append(ratio)

    avg_ratio = np.average(ratios)
    if avg_ratio > 45:
        img = Image.fromarray(space)
        img.save(f"{PATH}{time}.png")


def calc_safety_factor(robots, height, width):

    space = np.zeros((height, width))
    for pos, _ in robots:
        space[pos[1], pos[0]] += 1

    q1 = np.sum(space[0:height // 2, 0:width // 2])
    q2 = np.sum(space[0:height // 2, width // 2 + 1:])
    q3 = np.sum(space[height // 2 + 1:, 0:width // 2])
    q4 = np.sum(space[height // 2 + 1:, width // 2 + 1:])

    return int(q1 * q2 * q3 * q4)


def main():

    with open("input.txt") as f:
        data = [line.strip() for line in f]

    robots = []
    for item in data:
        config = []
        for vec in item.split(" "):
            vec = [int(num) for num in vec[2:].split(",")]
            config.append(np.array(vec))
        robots.append(config)

    width, height = 101, 103

    for second in range(1, 7000):
        for pos, vel in robots:
            pos += vel
            pos %= np.array([width, height])

        if second == 100:
            safety_factor = calc_safety_factor(robots, height, width)

        store_img(robots, height, width, second)

    print(f"Part One: {safety_factor}")
    print("Part Two: Have a look at the folder :)")


if __name__ == "__main__":
    main()
