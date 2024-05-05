def calculate_scores(data):

    chars = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    scores = {
        ")": [3, 1],
        "]": [57, 2],
        "}": [1197, 3],
        ">": [25137, 4]
    }

    score1, scores2 = 0, []

    for line in data:

        corrupted = False

        needs_closing = []
        for char in line:
            if char in chars.keys():
                needs_closing.append(char)
            elif char in chars.values():
                if char == chars[needs_closing[-1]]:
                    del needs_closing[-1]
                else:
                    score1 += scores[char][0]
                    corrupted = True
                    break

        if not corrupted:
            needs_closing = [chars[char] for char in needs_closing[::-1]]

            score = 0
            for char in needs_closing:
                score *= 5
                score += scores[char][1]

            scores2.append(score)

    score2 = sorted(scores2)[int(len(scores2) / 2)]

    return score1, score2


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    score1, score2 = calculate_scores(data)

    print(f"Part One: {score1}")
    print(f"Part Two: {score2}")


if __name__ == "__main__":
    main()
