import re


def main():

    with open("input.txt") as f:
        data = f.readlines()

    data = [item.strip() for item in data]
    data = "".join(data)

    sum1, sum2 = 0, 0

    pattern = r"mul\([0-9]+,[0-9]+\)"
    matches = re.findall(pattern, data)

    for match in matches:
        nums = match[4:-1].split(",")
        sum1 += int(nums[0]) * int(nums[1])

    pattern = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, data)

    do = True
    for match in matches:

        if match == "do()":
            do = True

        elif match == "don't()":
            do = False

        elif do:
            nums = match[4:-1].split(",")
            sum2 += int(nums[0]) * int(nums[1])

    print(f"Part One: {sum1}")
    print(f"Part Two: {sum2}")


if __name__ == "__main__":
    main()
