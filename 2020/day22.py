import copy


def part_one(content):
    """Determine the winning player's score."""

    p1 = content[1:content.index('')]
    p2 = content[content.index('')+2:]

    p1 = [int(num) for num in p1]
    p2 = [int(num) for num in p2]

    while p1 and p2:
        p1Card = p1.pop(0)
        p2Card = p2.pop(0)

        if p1Card > p2Card:
            p1.append(p1Card)
            p1.append(p2Card)
        else:
            p2.append(p2Card)
            p2.append(p1Card)

    winnerDeck = p1 if len(p2) == 0 else p2
    winnerScore = 0

    i = 1
    for card in winnerDeck[::-1]:
        winnerScore += card * i
        i += 1

    return winnerScore


def part_two(content):
    """Determine the winning player's score with the new rules."""

    def subgame(player1, player2):
        previousP1 = [copy.deepcopy(player1)]
        previousP2 = [copy.deepcopy(player2)]

        start = True
        while len(player1) != 0 and len(player2) != 0:

            p1Card = player1.pop(0)
            p2Card = player2.pop(0)

            if int(p1Card) <= len(player1) and int(p2Card) <= len(player2):
                winner = subgame(
                    copy.deepcopy(player1[:int(p1Card)]),
                    copy.deepcopy(player2[:int(p2Card):])
                )
                if winner == 'p1':
                    player1.append(p1Card)
                    player1.append(p2Card)
                else:
                    player2.append(p2Card)
                    player2.append(p1Card)
            else:
                if int(p1Card) > int(p2Card):
                    player1.append(p1Card)
                    player1.append(p2Card)
                else:
                    player2.append(p2Card)
                    player2.append(p1Card)

            if (player1 in previousP1 or player2 in previousP2) and not start:
                return 'p1'
            start = False

            previousP1.append(copy.deepcopy(player1))
            previousP2.append(copy.deepcopy(player2))

        winner = 'p1' if len(player1) > len(player2) else 'p2'
        return winner

    p1 = content[1:content.index('')]
    p2 = content[content.index('')+2:]

    p1 = [int(num) for num in p1]
    p2 = [int(num) for num in p2]

    while p1 and p2:
        p1Card = p1.pop(0)
        p2Card = p2.pop(0)

        if int(p1Card) <= len(p1) and int(p2Card) <= len(p2):
            player1 = copy.deepcopy(p1[:int(p1Card)])
            player2 = copy.deepcopy(p2[:int(p2Card)])

            winner = subgame(player1, player2)

            if winner == 'p1':
                p1.append(p1Card)
                p1.append(p2Card)
            else:
                p2.append(p2Card)
                p2.append(p1Card)
        else:
            if int(p1Card) > int(p2Card):
                p1.append(p1Card)
                p1.append(p2Card)
            else:
                p2.append(p2Card)
                p2.append(p1Card)

    winner = p1 if len(p1) > len(p2) else p2
    score = 0

    i = 1
    for value in winner[::-1]:
        score += int(value) * i
        i += 1

    return score


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
