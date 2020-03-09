def chosen_weapon(num):
    if num == 1:
        return "Rock"
    if num == 2:
        return "Paper"
    if num == 3:
        return "Scissors"


def determine_winner(player_1, player_2):
    if player_1 == 1 and player_2 == 2:
        print("player2 wins!")
    elif player_2 == 1 and player_1 == 2:
        print("player1 wins!")
    elif player_1 == 3 and player_2 == 2:
        print("player1 wins!")
    elif player_2 == 3 and player_1 == 2:
        print("player2 wins!")
    elif player_1 == 1 and player_2 == 3:
        print("player1 wins!")
    elif player_2 == 1 and player_1 == 3:
        print("player2 wins!")
    elif player_1 == 4 or player_2 == 4:
        return 4
    else:
        print("TIE!")


def rock_paper_scissors():
    print("Type 4 to quit\n")
    player_1 = int(input("Please input your chosen weapon\n"))
    player_2 = int(input("Please input your chosen weapon\n"))
    while determine_winner(player_1, player_2) != 4:
        rock_paper_scissors()


def main():
    rock_paper_scissors()


if __name__ == '__main__':
    main()
