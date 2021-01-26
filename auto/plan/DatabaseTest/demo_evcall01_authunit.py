# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.rescources.DatabaseTest.conf_db import auth_unit

from auto.conftest import database_connector

from utils.myassert import for_assertTrue

def test_authunit_columns_exist(database_connector):

    for_assertTrue(database_connector.has_columns(auth_unit["table_name"], auth_unit["columns"]))

def test_authunit_primary_key(database_connector):

    for_assertTrue(database_connector.is_primary_key(auth_unit["table_name"], auth_unit["primary_key"]))

def test_authunit_nullable(database_connector):

    for_assertTrue(database_connector.is_nullable(auth_unit["table_name"], auth_unit["nullable"]))

def test_authunit_default(database_connector):

    for_assertTrue(database_connector.is_default(auth_unit["table_name"], auth_unit["default"]))