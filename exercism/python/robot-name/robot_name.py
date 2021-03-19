from string import ascii_uppercase, digits
import random


class Robot:
    def __init__(self):
        uppercase_ = random.choices(ascii_uppercase, k=2)
        digits_ = random.choices(digits, k=3)

        self.name = ''.join(uppercase_ + digits_)

    def reset(self):
        self.__init__()
