def getCountMatchingCards(winningNums, cardNums):

    count = 0
    for card in cardNums:
        if card in winningNums:
            count += 1

    return count


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    cards = dict()

    sum_ = 0
    for card in data:

        winningNums = card.split(": ")[1].split(" | ")[0].split(" ")
        winningNums = [int(num) for num in winningNums if num != ""]
        cardNums = card.split(": ")[1].split(" | ")[1].split(" ")
        cardNums = [int(num) for num in cardNums if num != ""]

        id_ = int(card.split(": ")[0].split("Card ")[1])
        cards[id_] = [1, winningNums, cardNums]

        count = getCountMatchingCards(winningNums, cardNums)
        sum_ += 0 if count == 0 else 2**(count - 1)

    print(f"Part One: {sum_}")

    sum_ = 0
    for id_ in cards.keys():

        sum_ += cards[id_][0]

        count = getCountMatchingCards(cards[id_][1], cards[id_][2])
        for i in range(1, count + 1):
            cards[id_ + i][0] += cards[id_][0]

    print(f"Part Two: {sum_}")


if __name__ == "__main__":
    main()
