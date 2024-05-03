# HINT: I used code from the below link in order to solve part two.
# LINK: https://0xdf.gitlab.io/adventofcode2020/13

from functools import reduce


def part_one(content):
    """Find the earliest bus you can take."""

    time = int(content[0])
    time_init = int(content[0])
    busses = content[1].split(',')
    busses = [int(bus) for bus in busses if bus != "x"]

    result = None
    while True:
        for bus in busses:
            if time % bus == 0:
                result = bus
                break

        if result:
            break

        time += 1

    time_to_wait = time - time_init

    result = time_to_wait * result

    return result


def part_two(content):
    """Find the earliest timestamp for all busses to depart with the offset."""

    def remainder(n, a):

        sum_, prod = 0, reduce(lambda a, b: a*b, n)

        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum_ += a_i * mul_inv(p, n_i) * p

        return sum_ % prod

    def mul_inv(a, b):

        b0 = b
        x0, x1 = 0, 1

        if b == 1:
            return 1

        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0

        if x1 < 0:
            x1 += b0

        return x1

    content[1] = content[1].split(",")

    busses = [int(b) for b in content[1] if b != "x"]
    offsets = [int(b) - i for i, b in enumerate(content[1]) if b != "x"]

    return remainder(busses, offsets)


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
