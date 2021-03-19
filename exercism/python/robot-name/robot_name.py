from string import ascii_uppercase, digits
import random


class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        self.__init__()

    def generate_name(self):
        random.seed()
        uppercase_ = random.choices(ascii_uppercase, k=2)
        digits_ = random.choices(digits, k=3)

        return ''.join(uppercase_ + digits_)
