# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"


from auto.rescources.DatabaseTest.conf_db import auth_sys_user

from auto.conftest import database_connector

from utils.myassert import for_assertTrue

def test_authsysuser_columns_exist(database_connector):

    for_assertTrue(database_connector.has_columns(auth_sys_user["table_name"], auth_sys_user["columns"]))

def test_authsysuser_primary_key(database_connector):

    for_assertTrue(database_connector.is_primary_key(auth_sys_user["table_name"], auth_sys_user["primary_key"]))

def test_authsysuser_nullable(database_connector):

    for_assertTrue(database_connector.is_nullable(auth_sys_user["table_name"], auth_sys_user["nullable"]))

def test_authsysuser_default(database_connector):

    for_assertTrue(database_connector.is_default(auth_sys_user["table_name"], auth_sys_user["default"]))