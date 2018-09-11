from string import ascii_letters, digits
from random import choice


def w_generator(*args, **kwargs):
    return choice(ascii_letters)


def d_generator(*args, **kwargs):
    return choice(digits)
