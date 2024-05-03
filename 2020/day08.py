def part_one(content):
    """Find the value in the accumulator."""

    acc = 0

    i, visited = 0, []
    while True:
        if i in visited or i >= len(content):
            break
        visited.append(i)

        op = content[i].split(' ')[0]
        val = int(content[i].split(' ')[1])

        if op == 'acc':
            acc += val
            i += 1
        elif op == 'jmp':
            i += val
        else:
            i += 1

    return acc


def part_two(content):
    """Change one instruction so the code will terminate."""

    def checkForLoop(content):
        i, visited = 0, []
        while True:
            if i in visited:
                return True
            visited.append(i)
            if i >= len(content):
                return False

            op = content[i].split(' ')[0]
            val = int(content[i].split(' ')[1])

            if op == 'jmp':
                i += val
            else:
                i += 1

    i = 0
    while True:
        op = content[i].split(' ')[0]
        if op == 'acc':
            i += 1
            continue
        else:
            changedContent = content.copy()
            if op == 'nop':
                changedContent[i] = 'jmp ' + changedContent[i].split(' ')[1]
            elif op == 'jmp':
                changedContent[i] = 'nop ' + changedContent[i].split(' ')[1]
            if not checkForLoop(changedContent):
                break
        i += 1

    return part_one(changedContent)


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
