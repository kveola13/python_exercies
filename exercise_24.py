def draw_game_board(amount_of_rows):
    print(" --- --- --- ")
    for num in range(amount_of_rows):
        print("|   |   |   |")
        print(" --- --- --- ")


def main():
    draw_game_board(3)


if __name__ == '__main__':
    main()
