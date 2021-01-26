# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

"""
    runner.runner.py单元测试
"""
import sys
import os
from unittest import runner
curpath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curpath)[0]
sys.path.append(rootPath)

import unittest
from runner.DBRunner import DBRunner

class TestDBRunner(unittest.TestCase):
    conn_str = "mysql+pymysql://root:123456@localhost:3306/autolab"
    table_name = "demo"
    def test_has_columns(self):
        runner = DBRunner(self.conn_str)

        columns = ["id", "user", "name", "unique_id", "test"]
        # columns = ["id", "user", "name", "unique_id", "test"]

        res = runner.has_columns(self.table_name, columns)
        for col in columns:
            print("Has column: %s -> %s" %(col, res[col]))
            assert res[col] == True
        
    def test_is_primary_key(self):
        runner = DBRunner(self.conn_str)
        p_k = ["id", "name"]
        res = runner.is_primary_key(self.table_name, p_k)
        for  p in p_k:
            print("%s is primary key -> %s" %(p, res[p]))
            assert res[p] == True

if __name__ == '__main__':
    unittest.main()

