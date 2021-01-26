__author__ = "YuKwengRu"

import pytest

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf import AUTOLAB

def test_autolab_tables(database_connector):
    db = database_connector

    res = db.has_tables(AUTOLAB["tables"])

    for table in AUTOLAB["tables"]:
        print("table %s in database!" % table)

        assert res[table]