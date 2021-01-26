# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import pytest

from auto.conftest import database_connector

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf import AUTOLAB_DEMO

def test_demo_columns_exist(database_connector):
    db = database_connector

    res = db.has_columns(AUTOLAB_DEMO["table_name"], AUTOLAB_DEMO["columns"])
    for col in AUTOLAB_DEMO["columns"]:
        print("exist column: %s --> %s" %(col, res[col]))

        assert res[col]

def test_demo_primary_key(database_connector):
    db = database_connector

    res = db.is_primary_key(AUTOLAB_DEMO["table_name"], AUTOLAB_DEMO["primary_key"])

    for col in AUTOLAB_DEMO["primary_key"]:
        print("exist primary key: %s --> %s" %(col, res[col]))

        assert res[col]

def test_authauthority_default(database_connector):
    db = database_connector

    res = db.is_default(AUTOLAB_DEMO["table_name"], AUTOLAB_DEMO["default"])
    print(AUTOLAB_DEMO["default"])

    for col in AUTOLAB_DEMO["default"]:
        print(col)
        k,v = col.popitem()
        print("table %s  column %s has default? %s" % (AUTOLAB_DEMO["table_name"],k, res[k]))

        assert res[k]