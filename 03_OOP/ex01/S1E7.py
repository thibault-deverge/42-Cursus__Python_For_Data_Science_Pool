from S1E9 import Character


class Baratheon(Character):
    """Character representing Baratheon family"""

    def __init__(self, first_name, is_alive=True, eyes='brown', hairs='dark'):
        '''Initialize Baratheon character'''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        '''Return string representation of Baratheon character'''
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        '''Return string representation of Baratheon character'''
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def die(self):
        '''Kill the Baratheron by changing alive boolean to False.'''
        self.is_alive = False


class Lannister(Character):
    """Character representing Lannister family"""

    def __init__(self, first_name, is_alive=True, eyes='blue', hairs='light'):
        '''Initialize Baratheon character'''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        '''Return string representation of Lannister character'''
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        '''Return string representation of Lannister character'''
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        '''Alternative constructor to create an instance of Lannister'''
        return cls(first_name, is_alive)

    def die(self):
        '''Kill the Lannister by changing alive boolean to False.'''
        self.is_alive = False
