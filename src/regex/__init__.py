# -*- coding: utf-8 -*-
import re
from sre_constants import error

from faker.providers import BaseProvider

from .generators import (
    w_generator,
    d_generator,
)


MAPPING = {
    r'\w': w_generator,
    r'\d': d_generator,
}


class RegexParser(object):
    def __init__(self, pattern):
        self.pos = 0
        self.pattern = pattern

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.pattern):
            raise StopIteration

        char = self.pattern[self.pos]
        self.pos += 1
        return char

    def _get_next_block(self):
        self.pos += 1
        if self.pos > len(self.pattern):
            raise StopIteration
        yield self.pattern[self.pos]


class RegexProvider(BaseProvider):
    """
    A Provider for regular expressions related test data.

    >>> from faker import Faker
    >>> from faker_web import RegexProvider
    >>> fake = Faker()
    >>> fake.add_provider(RegexProvider)
    """

    def regex(self, pattern):
        """
        Returns a .
        >>> pattern = r'\w\w\wo\d'
        >>> fake.regex(pattern)
        helo2

        :return: string that fits pattern
        :rtype: str
        """
        try:
            re.compile(pattern)
        except error as e:
            raise ValueError(
                'Invalid pattern provided. '
                'Please make sure your data is not corrupted: %s' % e)
        result = ''
        parser = RegexParser(pattern)
        import pdb; pdb.set_trace()
        for block in parser:
            print(block)
        # import pdb; pdb.set_trace()
        return ''

