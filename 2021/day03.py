import numpy as np


def binary_to_decimal(binary):

    decimal = 0
    for i, val in enumerate(binary[::-1]):
        decimal += val * 2**i

    return decimal


def part_one(data):

    gamma_rate_binary = []
    for col in range(data.shape[1]):

        ones = np.sum(data[:, col])
        zeros = data.shape[0] - ones

        gamma_val = 1 if ones > zeros else 0
        gamma_rate_binary.append(gamma_val)

    gamma_rate_decimal = binary_to_decimal(gamma_rate_binary)
    epsilon_rate_decimal = binary_to_decimal(1 - np.array(gamma_rate_binary))

    return gamma_rate_decimal * epsilon_rate_decimal


def part_two(data):

    def calculate_rating(array, mode):

        for col in range(data.shape[1]):

            ones = np.sum(array[:, col])
            zeros = array.shape[0] - ones

            if mode == "mcb":
                criteria = 1 if ones >= zeros else 0
            elif mode == "lcb":
                criteria = 1 if ones < zeros else 0
            array = array[np.where(array[:, col] == criteria)]

            if array.shape[0] == 1:
                break

        return binary_to_decimal(array.flatten())

    og_decimal = calculate_rating(data, "mcb")
    co2_decimal = calculate_rating(data, "lcb")

    return og_decimal * co2_decimal


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    data = [list(item) for item in data]
    data = np.array(data, dtype=int)

    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")


if __name__ == "__main__":
    main()
