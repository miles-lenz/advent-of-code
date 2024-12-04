def determine_type(hand):

    # meaning of return values:
    # 1 = five of a kind
    # 2 = four of a kind
    # ...
    # 7 = high card

    len_unique = len(set(hand))

    if len_unique == 2:
        count_max = hand.count(max(set(hand), key=hand.count))
        return 2 if count_max == 4 else 3

    if len_unique == 3:
        count_max = hand.count(max(set(hand), key=hand.count))
        return 4 if count_max == 3 else 5

    if len_unique in [2, 3]:
        count_max = hand.count(max(set(hand), key=hand.count))
        return [2 if count_max == 4 else 3, 2 + count_max][len_unique - 2]

    if len_unique in [4, 5]:
        return len_unique + 2

    return len_unique


def sort(sorted_, labels, hand, bid, type_):

    for i, (c_hand, _, c_type) in enumerate(sorted_):

        if c_type < type_:
            continue

        if c_type > type_:
            sorted_.insert(i, (hand, bid, type_))
            return

        for j in range(5):

            if c_hand[j] == hand[j]:
                continue

            if labels.index(c_hand[j]) < labels.index(hand[j]):
                break

            sorted_.insert(i, (hand, bid, type_))
            return

    sorted_.append((hand, bid, type_))


def part_one(data):

    labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    unsorted = []
    for hand, bid in data:
        type_ = determine_type(hand)
        unsorted.append((hand, bid, type_))

    sorted_ = []
    for hand, bid, type_ in unsorted:
        sort(sorted_, labels, hand, bid, type_)
    sorted_ = sorted_[::-1]

    total_winnings = 0
    for i, (_, bid, _) in enumerate(sorted_):
        total_winnings += (i + 1) * bid

    return total_winnings


def main():

    with open("input.txt") as f:
        data = f.readlines()

    data = [item.strip().split(" ") for item in data]
    data = [[x, int(y)] for x, y in data]

    print(f"Part One: {part_one(data)}")


if __name__ == "__main__":
    main()
