def tic_tac_toe(row, column):
    game_board = [[0] * row for num in range(column)]
    return game_board


def check_game_is_won(game_board):
    for num in range(0, len(game_board)):
        row = {game_board[num][0], game_board[num][1], game_board[num][2]}
        if len(row) == 1 and game_board[num][0] != 0:
            return game_board[num][0]
    for num in range(0, len(game_board)):
        column = [game_board[0][num], game_board[1][num], game_board[2][num]]
        if len(column) == 1 and game_board[0][num] != 0:
            return game_board[0][num]
    first_across = {game_board[0][0], game_board[1][1], game_board[2][2]}
    second_across = {game_board[0][2], game_board[1][1], game_board[2][0]}
    if len(first_across) == 1 or len(second_across) == 1 and game_board[1][1] != 0:
        return game_board[1][1]
    return 0


def main():
    game_board = [[2, 2, 1],
                  [2, 1, 2],
                  [1, 1, 1]]
    print(check_game_is_won(tic_tac_toe(3, 3)))
    print(check_game_is_won(game_board))


if __name__ == '__main__':
    main()
