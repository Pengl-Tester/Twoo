# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

"""
    数据库测试驱动
"""

# for database
from sqlalchemy import create_engine 
from sqlalchemy.engine import reflection
from sqlalchemy.dialects.mysql import *

from .runner import Runner

class DBRunner(Runner):
    
    def __init__(self, conn_str="", encoding="utf-8", echo=False):
        super().__init__(name = "DataBase Runner")

        # init engine object
        engine = create_engine(conn_str, encoding=encoding, echo=echo)

        # init inspector object
        self.insp = reflection.Inspector.from_engine(engine)

    def has_tables(self, tables_name=[]):
        res = {}

        tables = self.insp.get_table_names()

        for table in tables_name:
            if table in tables:
                res[table] = True
            else:
                res[table] = False
        
        return res
    
    def has_columns(self, table_name, columns_name=[]):
        res = {}
        for col in columns_name:
            res[col] = self.__find_column(table_name, col) != None
        
        return res
    
    def is_primary_key(self, table_name, columns_name=[]):
        res = {}

        keys = self.insp.get_pk_constraint(table_name)
        for  col in columns_name:
            res[col] = col in keys["constrained_columns"]
        
        return res
    
    def is_unique(self, table_name, columns_name=[]):
        res = {}
        unique_columns = self.insp.get_unique_constraints(table_name)
        for col in columns_name:
            res[col] = False
            for unique in unique_columns:
                if col in unique["column_names"]:
                    res[col] = True
                    break
        return res
    
    def has_index(self, table_name, columns_name = []):
        res = {}

        indexes = self.insp.get_indexes(table_name)
        for col in columns_name:
            res[col] = False
            for index in indexes:
                if col in index["column_names"]:
                    res[col] = True
                    break
        
        return res

    def is_nullable(self, table_name, columns_name=[]):
        res = {}
        for col in columns_name:
            res[col] = self.__find_column(table_name, col)["nullable"]
        
        return res
    
    def is_default(self, table_name, columns={}):
        res = {}
        for (k,v) in columns.items():
            # for (k,v) in col.items():
            #     # v = col[k]
            res[k] = v == self.__find_column(table_name, k)["default"]
            # for k in col.keys():
            #     v = col[k]
            #     res[k] = v == self.__find_column(table_name, k)["default"]
        
        return res
    
    def __find_column(self, table_name, column_name):
        columns = self.insp.get_columns(table_name)

        for col in columns:
            if column_name == col["name"]:
                return col
        
        return None