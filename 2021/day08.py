def part_one(data):

    count = 0
    for entry in data:

        output_value = entry.split(" | ")[1].split(" ")
        for digit in output_value:
            if len(digit) in [2, 4, 3, 7]:
                count += 1

    return count


def part_two(data):

    digits = {
        0: ["a", "b", "c", "e", "f", "g"],
        1: ["c", "f"],
        2: ["a", "c", "d", "e", "g"],
        3: ["a", "c", "d", "f", "g"],
        4: ["b", "c", "d", "f"],
        5: ["a", "b", "d", "f", "g"],
        6: ["a", "b", "d", "e", "f", "g"],
        7: ["a", "c", "f"],
        8: ["a", "b", "c", "d", "e", "f", "g"],
        9: ["a", "b", "c", "d", "f", "g"],
    }

    sum_ = 0
    for entry in data:

        mapping = {}
        for i in ["a", "b", "c", "d", "e", "f", "g"]:
            mapping[i] = set()

        signal_patterns = entry.split(" | ")[0].split(" ")
        output_value = entry.split(" | ")[1].split(" ")

        signal_patterns = sorted(signal_patterns, key=lambda x: len(x))

        one = set(signal_patterns.pop(0))
        seven = set(signal_patterns.pop(0))

        mapping["a"] = seven - one
        mapping["c"], mapping["f"] = one, one

        four = set(signal_patterns.pop(0))
        mapping["b"], mapping["d"] = four - one, four - one

        for pattern in signal_patterns:
            diff = set(pattern) - (mapping["a"] | mapping["b"] | mapping["c"])
            if len(pattern) == 6 and len(diff) == 1:
                mapping["g"] = diff
                signal_patterns.remove(pattern)

        eight = set(signal_patterns.pop(-1))
        mapping["e"] = eight - (seven | mapping["b"] | mapping["g"])

        for pattern in signal_patterns:
            diff = set(pattern) - (mapping["a"] | mapping["g"] | mapping["c"])
            if len(pattern) == 5 and len(diff) == 1:
                mapping["d"] = diff
                mapping["b"] = mapping["b"] - diff

        for pattern in signal_patterns:
            union = mapping["a"] | mapping["g"] | mapping["b"] | mapping["d"]
            diff = set(pattern) - union
            if len(pattern) == 5 and len(diff) == 1:
                mapping["f"] = diff
                mapping["c"] = mapping["c"] - diff

        mapped_digits = {}
        for key, val in digits.items():
            mapped_digits[key] = set()
            for v in val:
                mapped_digits[key].add(list(mapping[v])[0])

        num = ""
        for out in output_value:
            for key, val in mapped_digits.items():
                if val == set(out):
                    num += str(key)
        sum_ += int(num)

    return sum_


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")


if __name__ == "__main__":
    main()
