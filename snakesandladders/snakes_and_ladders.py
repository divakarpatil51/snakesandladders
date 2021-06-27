
from board import Board
from dice_factory import DiceFactory
from player import Player


def main():
    board = Board()
    board.initialize()
    player_name = input("Please enter player name: ")
    player = Player(player_name)
    dice = DiceFactory.get_dice()
    turns = 10
    while turns != 0:
        user_inp = input("\nPress R/r to roll the dice: ")
        if user_inp.lower() != 'r':
            print("Please enter valid value")
            continue
        turns -= 1
        roll_pos = dice.roll()
        curr_pos = player.get_current_pos()
        next_pos = curr_pos + roll_pos
        win, next_pos = board.validate_pos(next_pos)
        if win:
            break
        player.move_to(next_pos)
    else:
        print("You lost! Better Luck next time!")


if __name__ == '__main__':
    main()
