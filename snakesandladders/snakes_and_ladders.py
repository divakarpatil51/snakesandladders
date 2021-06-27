
from board import Board
from player import Player
from dice import Dice


def main():
    player_name = input("Please enter player name: ")
    board = Board()
    player = Player(player_name)
    turns = 10
    while turns != 0:
        user_inp = input("\nPress R/r to roll the dice: ")
        if user_inp.lower() != 'r':
            print("Please enter valid value")
            continue
        turns -= 1
        roll_pos = Dice.roll()
        curr_pos = player.get_current_pos()
        next_pos = curr_pos + roll_pos
        win = board.validate_pos(next_pos)
        if win:
            break
        player.move_to(next_pos)


if __name__ == '__main__':
    main()
