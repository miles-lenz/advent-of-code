from collections import defaultdict
from sympy import solve, Eq, Symbol


def main():

    with open("input.txt") as f:
        data = [line.strip() for line in f]

    tokens = defaultdict(int)
    for i in range(0, len(data), 4):

        btn_a = [int(n[2:]) for n in data[i].split(": ")[1].split(", ")]
        btn_b = [int(n[2:]) for n in data[i + 1].split(": ")[1].split(", ")]

        prize1 = [int(n[2:]) for n in data[i + 2].split(": ")[1].split(", ")]
        prize2 = [prize1[0] + 10000000000000, prize1[1] + 10000000000000]

        a, b = Symbol("a", integer=True), Symbol("b", integer=True)

        for i, prize in enumerate([prize1, prize2]):

            eq1 = Eq(a * btn_a[0] + b * btn_b[0], prize[0])
            eq2 = Eq(a * btn_a[1] + b * btn_b[1], prize[1])
            result = solve([eq1, eq2])

            if result == [] or i == 0 and (result[a] > 100 or result[b] > 100):
                continue

            tokens[i] += result[a] * 3 + result[b]

    print(f"Part One: {tokens[0]}")
    print(f"Part Two: {tokens[1]}")


if __name__ == "__main__":
    main()
