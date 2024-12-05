from collections import defaultdict as def_dict


def main():

    with open("input.txt") as f:
        data = [line.strip() for line in f]

    rules = data[:data.index("")]
    updates = data[data.index("") + 1:]
    updates = [item.split(",") for item in updates]

    before, after = def_dict(list), def_dict(list)
    for rule in rules:
        left, right = rule.split("|")
        before[right].append(left)
        after[left].append(right)

    incorrect_updates = []

    count1 = 0
    for update in updates:

        update_valid = True
        for i, num in enumerate(update):

            update_before = update[:i]
            update_after = update[i + 1:]

            cond1 = all(item in before[num] for item in update_before)
            cond2 = all(item in after[num] for item in update_after)

            if not (cond1 and cond2):
                update_valid = False
                incorrect_updates.append(update)
                break

        if update_valid:
            count1 += int(update[int(len(update)/2)])

    count2 = 0
    for update in incorrect_updates:

        new_oder = [update[0]]
        for num in update[1:]:

            for i, item in enumerate(new_oder):

                if num in after[item]:
                    continue

                new_oder.insert(i, num)
                break

            if num not in new_oder:
                new_oder.append(num)

        count2 += int(new_oder[int(len(new_oder)/2)])

    print(f"Part One: {count1}")
    print(f"Part Two: {count2}")


if __name__ == "__main__":
    main()
