# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.rescources.DatabaseTest.conf_db import auth_permit_user

from auto.conftest import database_connector

from utils.myassert import for_assertTrue

def test_authpermituser_columns_exist(database_connector):

    for_assertTrue(database_connector.has_columns(auth_permit_user["table_name"], auth_permit_user["columns"]))

def test_authpermituser_primary_key(database_connector):

    for_assertTrue(database_connector.is_primary_key(auth_permit_user["table_name"], auth_permit_user["primary_key"]))

def test_authpermituser_nullable(database_connector):

    for_assertTrue(database_connector.is_nullable(auth_permit_user["table_name"], auth_permit_user["nullable"]))

def test_authpermituser_default(database_connector):

    for_assertTrue(database_connector.is_default(auth_permit_user["table_name"], auth_permit_user["default"]))
