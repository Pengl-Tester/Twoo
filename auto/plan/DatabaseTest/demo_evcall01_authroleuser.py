# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"


from auto.conftest import database_connector

from auto.rescources.DatabaseTest.conf_db import auth_role_user

from utils.myassert import for_assertTrue

def test_authroleuser_columns_exist(database_connector):

    for_assertTrue(database_connector.has_columns(auth_role_user["table_name"], auth_role_user["columns"]))

def test_authroleuser_primary_key(database_connector):

    for_assertTrue(database_connector.is_primary_key(auth_role_user["table_name"], auth_role_user["primary_key"]))

def test_authroleuser_nullable(database_connector):

    for_assertTrue(database_connector.is_nullable(auth_role_user["table_name"], auth_role_user["nullable"]))

def test_authroleuser_default(database_connector):

    for_assertTrue(database_connector.is_default(auth_role_user["table_name"], auth_role_user["default"]))