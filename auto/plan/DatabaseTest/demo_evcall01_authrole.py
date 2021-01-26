# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

from auto.conftest import database_connector

from auto.rescources.DatabaseTest.conf_db import auth_role

from utils.myassert import for_assertTrue


def test_authrole_columns_exist(database_connector):

    for_assertTrue(database_connector.has_columns(auth_role["table_name"], auth_role["columns"]))

def test_authrole_primary_key(database_connector):

    for_assertTrue(database_connector.is_primary_key(auth_role["table_name"], auth_role["primary_key"]))

def test_authrole_nullable(database_connector):

    for_assertTrue(database_connector.is_nullable(auth_role["table_name"], auth_role["nullable"]))

def test_authrole_default(database_connector):

    for_assertTrue(database_connector.is_default(auth_role["table_name"], auth_role["default"]))
