import re


def part_one(content):
    """Evalute each equation with new math rules."""

    content = content.copy()

    def solve(equation):
        equation = equation.split(' ')

        while '+' in equation or '*' in equation:
            sol = eval(' '.join(equation[:3]))
            equation = [str(sol)] + equation[3:]

        return equation[0]

    for i, equation in enumerate(content):
        while '(' in equation:
            regex = re.search(r'\(([0-9]|\+|\*|\s)*\)', equation)
            subEqaution = regex.group()
            subIndex = regex.span()

            result = solve(subEqaution[1:-1])

            equation = (equation[:subIndex[0]] + result +
                        equation[subIndex[1]:])

        content[i] = int(solve(equation))

    result = sum(content)

    return result


def part_two(content):
    """Evalute each equation with addition before multiplication."""

    def solve(equation):
        equation = equation.split(' ')

        while '+' in equation:
            plusIndex = equation.index('+')
            sol = eval(' '.join(equation[plusIndex-1:plusIndex+2]))
            equation = (equation[:plusIndex-1] + [str(sol)] +
                        equation[plusIndex+2:])

        result = eval(' '.join(equation))

        return result

    for i, equation in enumerate(content):
        while '(' in equation:
            regex = re.search(r'\(([0-9]|\+|\*|\s)*\)', equation)
            subEq = regex.group()
            subEqIn = regex.span()

            subRes = str(solve(subEq[1:-1]))
            equation = equation[:subEqIn[0]] + subRes + equation[subEqIn[1]:]

        content[i] = int(solve(equation))

    return sum(content)


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
