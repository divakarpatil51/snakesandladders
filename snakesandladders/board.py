class Board:

    def __init__(self):
        self.size = 100

    def validate_pos(self, next_pos):
        if next_pos >= self.size:
            print("You won!!")
            return True
        return False
