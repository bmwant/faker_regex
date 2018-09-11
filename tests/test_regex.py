# -*- coding: utf-8 -*-
import re

from src.regex import RegexProvider  # noqa


def _check_match(result, pattern):
    return re.match(pattern, result) is not None


def test_one_word_character_generation(fake):
    pattern1 = r'\w\w\w'
    res1 = fake.regex(pattern1)
    # assert _check_match(res1, pattern1)


def test_one_digit_generation(fake):
    pass

