__author__ = "YuKwengRu"

import pytest

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf_db import EV_CALL_01

from utils.myassert import for_assertTrue

from utils.notify import send_dingtalk_msg

def test_evcall01_tables(database_connector, valid_tables_name_fix):

    tables, vdc = valid_tables_name_fix
    for_assertTrue("test_evcall01_tables", database_connector.has_tables(tables))

def test_primarykey(database_connector, valid_tables_name_fix, valid_tables_primary_key_fix):
    tables_primary_key = valid_tables_primary_key_fix
    tables, vdc = valid_tables_name_fix
    for table in tables:
        for_assertTrue("test_primarykey \n TABLE: %s \n " %table, database_connector.is_primary_key(table ,tables_primary_key[table]))

def test_columns(database_connector, valid_tables_name_fix, valid_tables_columns_fix):
    tables, vdc = valid_tables_name_fix
    tables_columns = valid_tables_columns_fix

    for table in  tables:
        for col in tables_columns[table]:
            for_assertTrue("test_columns \n TABLE: %s \n " %table, database_connector.has_columns(table, tables_columns[table]))

def test_uniques(database_connector, valid_tables_name_fix, valid_tables_unique_cols_fix):
    tables, vdc = valid_tables_name_fix
    tables_unique_cols = valid_tables_unique_cols_fix

    for table in tables:
        for_assertTrue("test_uniques \n TABLE: %s \n " %table, database_connector.is_unique(table, tables_unique_cols[table]))

def test_indexs(database_connector, valid_tables_name_fix, valid_tables_index_cols_fix):
    tables, vdc = valid_tables_name_fix
    tables_index_cols = valid_tables_index_cols_fix

    for table in tables:
        res = database_connector.has_index(table, tables_index_cols[table])
        for_assertTrue("test_indexs \n TABLE: %s \n " %table, res)

def test_nuls(database_connector, valid_tables_name_fix, valid_tables_nullable_cols_fix):
    tables, vdc = valid_tables_name_fix
    tables_nullable_cols = valid_tables_nullable_cols_fix

    for table in tables:
        res = database_connector.is_nullable(table, tables_nullable_cols[table])
        for_assertTrue("test_nuls \n TABLE: %s \n " %table, res)

def test_default(database_connector, valid_tables_name_fix, valid_tables_default_cols_fix):
    tables, vdc = valid_tables_name_fix
    tables_default_cols = valid_tables_default_cols_fix

    for table in tables:
        res = database_connector.is_default(table, tables_default_cols[table])
        for_assertTrue("test_default \n TABLE: %s \n " %table, res)