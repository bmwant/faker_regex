# -*- coding: utf-8 -*-
from faker.providers import BaseProvider

from .mimetypes import mime_types


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
        Returns a mime-type from the list of types understood by the Apache
        http server.
        >>> pattern =
        >>> fake.regex()
        application/mxf

        :return: content-type
        :rtype: str
        """
        return self.random_element(self.all_mime_types.keys())

