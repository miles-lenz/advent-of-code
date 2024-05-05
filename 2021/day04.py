import numpy as np


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    drawings = [int(item) for item in data[0].split(",")]
    boards = []

    current_board = []
    for line in data[2:]:
        if line == "":
            boards.append(np.array(current_board))
            current_board = []
        else:
            line = [int(item) for item in line.split(" ") if item != ""]
            current_board.append(line)
    boards.append(np.array(current_board))

    amount_boards = len(boards)

    winning_boards, winning_nums = [], []
    for num in drawings:

        new_boards = []
        for i, board in enumerate(boards):

            board[np.where(board == num)] = -1

            winning_col = np.any(np.all(board == -1, 0))
            winning_row = np.any(np.all(board == -1, 1))

            if winning_col or winning_row:
                winning_boards.append(np.copy(board))
                winning_nums.append(num)
            else:
                new_boards.append(board)

        boards = new_boards

        if len(winning_boards) == amount_boards:
            break

    winning_boards[0][np.where(winning_boards[0] == -1)] = 0
    winning_boards[-1][np.where(winning_boards[-1] == -1)] = 0

    part_one = np.sum(winning_boards[0]) * winning_nums[0]
    part_two = np.sum(winning_boards[-1]) * winning_nums[-1]

    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


if __name__ == "__main__":
    main()
