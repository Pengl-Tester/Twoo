# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.conftest import database_connector

from auto.rescources.DatabaseTest.conf_db import auth_permit_role

from utils.myassert import for_assertTrue

def test_authpermitrole_columns(database_connector):

    db = database_connector

    res = db.has_columns(auth_permit_role["table_name"], auth_permit_role["columns"])

    for_assertTrue(res)

def test_authpermitrole_primary_key(database_connector):

    db = database_connector

    res = db.is_primary_key(auth_permit_role["table_name"], auth_permit_role["primary_key"])

    for_assertTrue(res)

def test_authpermitrole_nullable(database_connector):

    res = database_connector.is_nullable(auth_permit_role["table_name"], auth_permit_role["nullable"])

    for_assertTrue(res)


def test_authpermitrole_default(database_connector):

    for_assertTrue(database_connector.is_default(auth_permit_role["table_name"], auth_permit_role["default"]))
