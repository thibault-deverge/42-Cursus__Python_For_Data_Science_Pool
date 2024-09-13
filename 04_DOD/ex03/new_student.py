import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generate random string id'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(self):
    '''Generate login 42 like'''
    return self.name[0:1] + self.surname[0:7]


@dataclass
class Student:
    '''data class student'''
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(default="", init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        '''init login after initial initialization from dataclass'''
        self.login = self.name[:1] + self.surname[:6]
