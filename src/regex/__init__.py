# -*- coding: utf-8 -*-
from faker.providers import BaseProvider

from .generators import (
    w_generator,
    d_generator,
)


MAPPING = {
    r'\w': w_generator,
    r'\d': d_generator,
}


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
        return ''

