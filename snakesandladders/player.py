
class Player:

    def __init__(self, name):
        self.name = name
        self.current_pos = 0

    def move_to(self, next_pos):
        self.current_pos = next_pos
        print(f"Player {self.name} moved to position: {self.current_pos}")

    def get_current_pos(self):
        return self.current_pos


