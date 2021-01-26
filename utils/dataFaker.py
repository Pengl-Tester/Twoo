# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

"""
    Faker Provider 插件
"""
from faker import Faker
from faker.providers import BaseProvider

import string

localized = True

class DataFaker(BaseProvider):

    def __init__(self):
        self.faker = Faker()