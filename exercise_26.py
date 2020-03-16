def draw_board(row, column):
    game_board = [[0] * row for num in range(column)]
    return game_board


def check_game_is_won(game_board):
    for num in range(0, len(game_board)):
        row = {game_board[num][0], game_board[num][1], game_board[num][2]}
        if len(row) == 1 and game_board[num][0] != 0:
            if game_board[num][0] == 0:
                return True, "Draw!"
            return False, "Player " + str(game_board[num][0]) + " wins!"
    for num in range(0, len(game_board)):
        column = [game_board[0][num], game_board[1][num], game_board[2][num]]
        if len(column) == 1 and game_board[0][num] != 0:
            if game_board[num][0] == 0:
                return True, "Draw!"
            return False, "Player " + str(game_board[num][0]) + " wins!"
    first_across = {game_board[0][0], game_board[1][1], game_board[2][2]}
    second_across = {game_board[0][2], game_board[1][1], game_board[2][0]}
    if len(first_across) == 1 or len(second_across) == 1 and game_board[1][1] != 0:
        if game_board[1][1] == 0:
            return True, "Draw!"
        return False, "Player " + str(game_board[1][1]) + " wins!"
    return False, "Keep playing"


def tic_tac_toe(game_board):
    game_board_copy = game_board
    player_x_turn = True
    player_coords = ""
    while check_game_is_won(game_board_copy) or check_game_is_won(game_board_copy) != 'Player 1 wins!' or \
            check_game_is_won(game_board_copy) != 'Player 2 wins!':
        print(check_game_is_won(game_board_copy))
        try:
            player_coords = tuple(
                map(int,
                    input("Please choose coordinates, separated with a comma:\nExit by typing 4,4\n").strip().split(
                        ',')))
        except ValueError:
            print("Invalid coordinates, try again")
            tic_tac_toe(game_board_copy)
        except IndexError:
            print("Invalid coordinates, try again")
            tic_tac_toe(game_board_copy)
        except TypeError:
            print("Invalid coordinates, try again")
            tic_tac_toe(game_board_copy)
        finally:
            if player_coords == (4, 4):
                break
            player_coords = (player_coords[0] - 1, player_coords[1] - 1)
            if player_x_turn and game_board_copy[player_coords[0]][player_coords[1]] == 0:
                game_board_copy[player_coords[0]][player_coords[1]] = 1
                player_x_turn = not player_x_turn
                print(game_board_copy)
            elif not player_x_turn and game_board_copy[player_coords[0]][player_coords[1]] == 0:
                game_board_copy[player_coords[0]][player_coords[1]] = 2
                player_x_turn = not player_x_turn
                print(game_board_copy)
    return game_board_copy


def main():
    game_board = [[2, 2, 1],
                  [2, 1, 2],
                  [1, 1, 1]]
    print(check_game_is_won(draw_board(3, 3)))
    print(check_game_is_won(game_board))
    print(tic_tac_toe(draw_board(3, 3)))


if __name__ == '__main__':
    main()
