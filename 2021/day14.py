def generate_polymer(template, rules, steps):

    pairs = {}
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        pairs[pair] = pairs[pair] + 1 if pair in pairs.keys() else 1

    n_rules = {}
    for rule in rules:
        pair, elm = rule.split(" -> ")
        n_rules[pair] = [pair[0] + elm, elm + pair[1]]
    rules = n_rules

    cnt = {}
    for letter in template:
        cnt[letter] = cnt[letter] + 1 if letter in cnt.keys() else 1

    for _ in range(steps):
        for pair, amount in pairs.copy().items():

            if amount == 0:
                continue

            pairs[pair] -= amount

            for n_pair in rules[pair]:
                cond = n_pair in pairs.keys()
                pairs[n_pair] = pairs[n_pair] + amount if cond else amount

            n_letter = rules[pair][0][1]
            cond = n_letter in cnt.keys()
            cnt[n_letter] = cnt[n_letter] + amount if cond else amount

    cnt = sorted(list(cnt.items()), key=lambda x: x[1])
    diff = cnt[-1][1] - cnt[0][1]

    return diff


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    template, rules = data[0], data[2:]

    print(f"Part One: {generate_polymer(template, rules, 10)}")
    print(f"Part Two: {generate_polymer(template, rules, 40)}")


if __name__ == "__main__":
    main()
