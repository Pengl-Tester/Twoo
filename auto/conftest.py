# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import pytest
from conf.configGlobal import DINGTALK_URL, DBURL, HTTPURL, VALIDDBURL, WSURL
from .rescources.DatabaseTest.conf_db import AUTOLAB, EV_CALL_01
from runner.DBRunner import DBRunner
from runner.HttpRunner import HttpRunner
from runner.WSRunner import WSRunner
from auto.rescources.ApiTest.conf_api import admin_login, agent_login, doctor_login, driver_login, create_task_help, is_work
from utils.assertAndNotify import assertAndNotify

'''
    dbtest fixture
'''
@pytest.fixture(scope="module")
def database_connector():

    return DBRunner(conn_str=DBURL)
    # return DBRunner(conn_str=AUTOLAB["conn_str"])

@pytest.fixture(scope="module")
def valid_db_connector():

    return DBRunner(conn_str=VALIDDBURL)

@pytest.fixture()
def valid_tables_name_fix(valid_db_connector, cache):
    vdc = valid_db_connector
    valid_tables = cache.get("tables", None)

    if valid_tables is None:
        print("no cache tables")
        valid_tables = vdc.insp.get_table_names()
        cache.set("tables", valid_tables)
        valid_tables = cache.get("tables", None)
    else:
        assert valid_tables

    return valid_tables, vdc

@pytest.fixture()
def valid_tables_primary_key_fix(valid_db_connector, cache):
    vdc = valid_db_connector
    tables = cache.get("tables", None)
    valid_tables_primary_key = cache.get("primary_key", None)

    if valid_tables_primary_key is None:
        valid_tables_primary_key = {}

        for table in tables:
            keys = vdc.insp.get_pk_constraint(table)
            valid_tables_primary_key[table] = keys["constrained_columns"]
    cache.set("primary_key", valid_tables_primary_key)
    valid_tables_primary_key = cache.get("primary_key", None)
    
    return valid_tables_primary_key

@pytest.fixture()
def valid_tables_columns_fix(valid_db_connector, cache):
    vdc = valid_db_connector
    tables = cache.get("tables", None)
    valid_tables_columns = cache.get("tables_columns", None)

    if valid_tables_columns is None:
        valid_tables_columns = {}

        for table in tables:
            columns = vdc.insp.get_columns(table)
            name = []
            for col in columns:
                name.append(col["name"])
            valid_tables_columns[table] = name
    cache.set("tables_columns", valid_tables_columns)
    valid_tables_columns = cache.get("tables_columns", None)

    return valid_tables_columns

@pytest.fixture()
def valid_tables_unique_cols_fix(valid_db_connector, cache):
    vdc = valid_db_connector
    tables = cache.get("tables", None)
    valid_unique_columns = cache.get("unique_columns", None)

    if valid_unique_columns is None:
        valid_unique_columns = {}

        for table in tables:
            uniques = vdc.insp.get_unique_constraints(table)
            # 这次操作是为了保留key
            valid_unique_columns[table] = uniques            
            for u in uniques:
                valid_unique_columns[table] = u["column_names"]
    cache.set("unique_columns", valid_unique_columns)
    valid_unique_columns = cache.get("unique_columns", None)
    
    return valid_unique_columns

@pytest.fixture()
def valid_tables_index_cols_fix(valid_db_connector, cache):
    vdc = valid_db_connector
    tables = cache.get("tables", None)
    valid_index_cols = cache.get("index_cols", None)

    if valid_index_cols is None:
        valid_index_cols = {}

        for table in tables:
            g = vdc.insp.get_indexes(table)
            index = []
            for i in g:
                col = i["column_names"]                
                for c in col:
                    index.append(c)
            valid_index_cols[table] = index
    cache.set("index_cols", valid_index_cols)
    valid_index_cols = cache.get("index_cols", None)

    return valid_index_cols

@pytest.fixture()             
def valid_tables_nullable_cols_fix(valid_db_connector, cache):
    vdc = valid_db_connector
    tables = cache.get("tables", None)
    valid_nullable_cols = cache.get("nullable_cols", None)

    if valid_nullable_cols is None:
        valid_nullable_cols = {}

        for table in tables:
            cols = vdc.insp.get_columns(table)
            nul = []
            for col in cols:
                if col["nullable"]  == True:
                    nul.append(col["name"])
            valid_nullable_cols[table] = nul
                
    cache.set("nullable_cols", valid_nullable_cols)
    valid_nullable_cols = cache.get("nullable_cols", None)
    return valid_nullable_cols

@pytest.fixture()             
def valid_tables_default_cols_fix(valid_db_connector, cache):
    vdc = valid_db_connector
    tables = cache.get("tables", None)
    valid_default_cols = cache.get("default_cols", None)

    if valid_default_cols is None:
        valid_default_cols = {}

        for table in tables:
            cols = vdc.insp.get_columns(table)
            defaults = {}
            for col in cols:
                defaults[col["name"]] = col["default"]
            valid_default_cols[table] = defaults
    cache.set("default_cols", valid_default_cols)
    valid_default_cols = cache.get("default_cols", None)
    return valid_default_cols

'''
    apitest fixture
'''
@pytest.fixture()
def http_connector_fix():

    hr = HttpRunner(base_url=HTTPURL, verify=False)
    # print("hc init success")
    return hr

@pytest.fixture
def admin_login_fix(http_connector_fix, cache):
    hr = http_connector_fix

    admin_token = cache.get("admin_token", None)
    if admin_token is None:
        print("no cache admin_token")
        res = hr.request(admin_login["method"], admin_login["uri"], params=admin_login["params"])
        rs = str(res)[-5:-2]
        if rs == "200":
            admin_token = res.json()["data"]["userInfo"]["token"]
            cache.set("admin_token", admin_token)
            admin_token = cache.get("admin_token", None)
        else:
            assertAndNotify(rs,"200", "admin_login_fix", rs)

    headers = {"token":admin_token}
    hr = HttpRunner(base_url=HTTPURL, verify=False, headers=headers)
    return hr, admin_token

@pytest.fixture
def agent_login_fix(http_connector_fix, cache):
    hr = http_connector_fix

    agent_token = cache.get("agent_token", None)
    if agent_token is None:
        print("no cache agent_token")
        res = hr.request(agent_login["method"], agent_login["uri"], params=agent_login["params"])
        rs = str(res)[-5:-2]
        rj = res.json()
        if rs == "200" and rj["code"] == 1:
            print(rj)
            agent_token = rj["data"]["userInfo"]["token"]
            cache.set("agent_token", agent_token)
            agent_token = cache.get("agent_token", None)
            print(agent_token)
        else:
            assertAndNotify(rs, "200", "agent_login_fix", rs)
            assertAndNotify(rj["code"], 1, "agent_login_fix", rj["msg"])

    headers = {"token":agent_token}
    hr = HttpRunner(base_url=HTTPURL, verify=False, headers=headers)
    return hr, agent_token

@pytest.fixture
def doctor_login_fix(http_connector_fix, cache):
    hr = http_connector_fix

    doctor_token = cache.get("doctor_token", None)
    if doctor_token is None:
        print("no cache doctor_token")
        res = hr.request(doctor_login["method"], doctor_login["uri"], params=doctor_login["params"])
        rs = str(res)[-5:-2]
        rj = res.json()
        if rs == "200" and rj["code"] == 1:
            doctor_token = res.json()["data"]["userInfo"]["token"]
            cache.set("doctor_token", doctor_token)
            doctor_token = cache.get("doctor_token", None)
        else:
            assertAndNotify(rs,"200", "agent_login_fix", rs)
            assertAndNotify(rj["code"], 1, "agent_login_fix", rj["msg"])
            

    headers = {"token":doctor_token}
    hr = HttpRunner(base_url=HTTPURL, verify=False, headers=headers)
    res = hr.request(is_work["method"], is_work["uri"])
    workstate = res.json()["data"]

    return hr, doctor_token, workstate

@pytest.fixture
def driver_login_fix(http_connector_fix, cache):
    hr = http_connector_fix

    driver_token = cache.get("driver_token", None)
    if driver_token is None:
        print("no cache driver_token")
        res = hr.request(driver_login["method"], driver_login["uri"], params=driver_login["params"])
        rs = str(res)[-5:-2]
        rj = res.json()
        if rs == "200" and rj["code"] == 1:
            driver_token = res.json()["data"]["userInfo"]["token"]
            cache.set("driver_token", driver_token)
            driver_token = cache.get("driver_token", None)
        else:
            assertAndNotify(rs,"200", "agent_login_fix", rs)
            assertAndNotify(rj["code"], 1, "agent_login_fix", rj["msg"])

    headers = {"token":driver_token}
    hr = HttpRunner(base_url=HTTPURL, verify=False, headers=headers)
    res = hr.request(is_work["method"], is_work["uri"])
    workstate = res.json()["data"]

    return hr, driver_token, workstate

@pytest.fixture
def create_task_help_fix(agent_login_fix, cache):

    hr, token = agent_login_fix

    help_id = cache.get("help_id", 0)
    first_dispatch_id = cache.get("first_dispatch_id", 0)
    if help_id == 0 or first_dispatch_id == 0:
        print("no cahce task")
        res = hr.request(create_task_help["method"], create_task_help["uri"], params = create_task_help["params"])
        rs = str(res)[-5:-2]
        rj = res.json()
        if rs == "200" and rj["code"] == 1:
            cache.set("help_id", rj["data"]["id"])
            cache.set("first_dispatch_id", rj["data"]["dispatchId"])
            help_id = cache.get("help_id", 0)
            first_dispatch_id = cache.get("first_dispatch_id", 0)
        else:
            assertAndNotify(rs,"200", "agent_login_fix", rs)
            assertAndNotify(rj["code"], 1, "agent_login_fix", rj["msg"])

    return hr, help_id, first_dispatch_id

'''
    websocket fixture
'''

@pytest.fixture
def web_socket_connector():

    return WSRunner(WSURL)

'''
    tcp fixture
'''
@pytest.fixture
def tcp_connector():
    pass

'''
    udp fixture
'''
@pytest.fixture
def udp_connector():
    pass

'''
    webdriver fixture
'''
@pytest.fixture
def web_connector():
    """
    return selenium webdriver object
    """
    pass