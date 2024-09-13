from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Character representing king of 7 kingdoms'''

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color
