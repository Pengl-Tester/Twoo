# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

from auto.conftest import database_connector

from auto.rescources.DatabaseTest.conf_db import auth_authority

from utils.myassert import for_assertTrue

def test_authauthority_columns_exist(database_connector):
    
    db = database_connector

    res = db.has_columns(auth_authority["table_name"], auth_authority["columns"])

    for_assertTrue(res)    
    
def test_authauthority_primary_key(database_connector):

    db = database_connector

    res = db.is_primary_key(auth_authority["table_name"], auth_authority["primary_key"])

    for_assertTrue(res)

def test_authauthority_nullable(database_connector):

    db = database_connector

    res = db.is_nullable(auth_authority["table_name"], auth_authority["nullable"])

    for_assertTrue(res)

def test_authauthority_default(database_connector):

    db = database_connector

    res = db.is_default(auth_authority["table_name"], auth_authority["default"])

    for_assertTrue(res)
    # d = auth_authority["default"]

    # for (k,v) in auth_authority["default"].items():
    #     # print(k)
    #     # print(v)
    #     # k,v = col.popitem()
    #     print("table %s  column %s has default? %s" % (auth_authority["table_name"],k, res[k]))

    #     assert res[k]