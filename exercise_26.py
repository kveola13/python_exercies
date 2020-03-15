def tic_tac_toe(row, column):
    game_board = [[0] * row for num in range(column)]
    return game_board


def check_game_is_won(game_board):
    count = 0
    for num in range(len(game_board)):
        for second_num in range(len(game_board[num])):
            game_board[num][second_num] = count
            count += 1
    return game_board


def main():
    # print(tic_tac_toe(3, 3))
    print(check_game_is_won(tic_tac_toe(3, 3)))


if __name__ == '__main__':
    main()
