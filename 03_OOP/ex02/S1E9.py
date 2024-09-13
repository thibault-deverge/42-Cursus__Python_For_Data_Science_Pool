from abc import ABC, abstractmethod


class Character(ABC):
    '''Abstract base class representing a character.'''

    def __init__(self, first_name, is_alive=True):
        '''Initialize a character with a first name and alive status.'''
        self.first_name = first_name
        self.is_alive = bool(is_alive)

    @abstractmethod
    def die(self):
        '''Abstract method which kill the character.'''
        pass


class Stark(Character):
    '''Class representing a Stark character, inheriting from Character.'''

    def __init__(self, first_name, is_alive=True):
        '''Initialize a Stark character by calling Character contructor.'''
        super().__init__(first_name, is_alive)

    def die(self):
        '''Kill the Stark by changing alive boolean to False.'''
        self.is_alive = False
