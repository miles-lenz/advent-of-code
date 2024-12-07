import itertools as it
import numpy as np


def calc(nums, op):

    result = nums[0]

    for i in range(len(op)):
        if op[i] == "+":
            result += nums[i+1]
        elif op[i] == "*":
            result *= nums[i+1]
        else:
            result = int(f"{result}{nums[i+1]}")

    return result


def check_equations(data, max_, part_one):

    symbols = ["+", "*"] if part_one else ["+", "*", "|"]

    operators = {}
    for i in range(1, max_ + 1):
        operators[i] = list(it.product(symbols, repeat=i))

    sum_ = 0
    for i, equation in enumerate(data):

        test_val = int(equation.split(": ")[0])
        nums = np.array(equation.split(": ")[1].split(" "), dtype=int)

        len_nums = len(nums) - 1
        for op in operators[len_nums]:

            val = calc(nums, op)

            if val == test_val:
                sum_ += test_val
                break

    return sum_


def main():

    with open("input.txt") as f:
        data = [line.strip() for line in f]

    max_ = 0
    for line in data:
        line = line.split(": ")[1].split(" ")
        max_ = max(max_, len(line) - 1)

    part_one = check_equations(data, max_, part_one=True)
    part_two = check_equations(data, max_, part_one=False)

    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
