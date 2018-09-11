# -*- coding: utf-8 -*-
import os
import pytest
import sys

from faker import Faker

from src.regex import RegexProvider  # noqa


@pytest.fixture(scope='module')
def fake():
    fixture = Faker()
    fixture.add_provider(RegexProvider)
    return fixture
