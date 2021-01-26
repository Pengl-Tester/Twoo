# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.rescources.DatabaseTest.conf_db import auth_system

from auto.conftest import database_connector

from utils.myassert import for_assertTrue

def test_authsystem_columns_exist(database_connector):

    for_assertTrue(database_connector.has_columns(auth_system["table_name"], auth_system["columns"]))

def test_authsystem_primary_key(database_connector):

    for_assertTrue(database_connector.is_primary_key(auth_system["table_name"], auth_system["primary_key"]))

def test_authsystem_nullable(database_connector):

    for_assertTrue(database_connector.is_nullable(auth_system["table_name"], auth_system["nullable"]))

def test_authsystem_default(database_connector):

    for_assertTrue(database_connector.is_default(auth_system["table_name"], auth_system["default"]))