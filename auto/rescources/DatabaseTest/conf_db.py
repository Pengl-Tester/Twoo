# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

import time

AUTOLAB = {
    "conn_str": "mysql+pymysql://root:jsfj120JSFJ!@)@192.168.2.230:3306/autolab",
    "encoding": "utf-8",
    "echo": False,
    "tables": ["demo"]
}

AUTOLAB_DEMO = {
    "table_name": "demo",
    "columns": ["id","user", "name", "unique_id"],
    "primary_key": ["id"],
    "nullable": ["id"],
    "unique": ["user", "unique_id"],
    "index": ["id", "user", "unique_id"],
    "default": [{"user": "ryk"},{"unique_id": None}]
}

EV_CALL_01 = {
    "conn_str": "mysql+pymysql://root:jsfj120JSFJ!@)@192.168.2.230:3306/ev-call-01",
    "encoding": "utf-8",
    "echo": False,
    "tables": ["auth_authority", "auth_permit_role", "auth_permit_user", "auth_role", "auth_role_user", ]
}

auth_authority = {
    "table_name": "auth_authority",
    "columns": [ "id", "code", "name", "parent_code", "parent_name", "icon", "href", "type", "status", "remark", "system_code", "system_name", "create_time", "creator", "update_time", "updater"],
    "primary_key": ["id"],
    "nullable": ["name", "parent_code", "parent_name", "icon", "href", "type", "status", "remark",  "create_time", "creator", "update_time", "updater"],
    "unique": [],
    "index": [""],
    "default": {"name":None,"parent_code":None,"parent_name":None, "icon":None, "href":None, "type":None, "status":None, "remark":None, "create_time":"CURRENT_TIMESTAMP", "creator":None, "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "updater":None}
}

    # "default": [{"name":None}, {"parent_code":None}, {"parent_name":None}, {"icon":None}, {"href":None}, {"type":None}, {"status":None}, {"remark":None}, {"create_time":"CURRENT_TIMESTAMP"}, {"creator":None}, {"update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"}, {"updater":None}]

auth_permit_role = {
    "table_name": "auth_permit_role",
    "columns": ["id","auth_code", "auth_name", "role_code", "role_name", "create_time", "creator", "update_time", "updater", "system_code", "system_name"],
    "primary_key": ["id"],
    "nullable": ["role_code", "role_name", "create_time", "creator", "update_time", "updater", "system_code", "system_name"],
    "unique": [],
    "index": [],
    "default": {"role_code":None, "role_name":None, "create_time":"CURRENT_TIMESTAMP", "creator":None, "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "updater":None, "system_code":None, "system_name":None}
}

auth_permit_user = {
    "table_name": "auth_permit_user",
    "columns": ["id","auth_code", "auth_name", "user_id", "user_name", "sort", "create_time", "creator", "update_time", "updater", "system_code", "system_name"],
    "primary_key": ["id"],
    "nullable": ["user_id", "user_name", "sort", "create_time", "creator", "update_time", "updater", "system_code", "system_name"],
    "unique": [],
    "index": [],
    "default": {"auth_name":None, "user_id":None, "user_name":None, "sort":None, "create_time":"CURRENT_TIMESTAMP", "creator":None, "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "updater":None, "system_code":None, "system_name":None}
}

auth_role = {
    "table_name": "auth_role",
    "columns": ["id","code", "name", "system_code", "system_name", "status", "unit_id", "unit_name", "remark", "create_time", "creator", "update_time", "updater"],
    "primary_key": ["id"],
    "nullable": ["status", "unit_id", "unit_name", "remark", "create_time", "creator", "update_time", "updater"],
    "unique": [],
    "index": [],
    "default": {"status":None, "unit_id":None, "unit_name":None, "remark":None, "create_time":"CURRENT_TIMESTAMP", "creator":None, "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "updater":None}
}


auth_role_user = {
    "table_name": "auth_role_user",
    "columns": ["id","role_code", "role_name", "user_id", "user_name", "create_time", "creator", "update_time", "updater", "system_code", "system_name"],
    "primary_key": ["id"],
    "nullable": ["role_code", "role_name", "user_id", "user_name", "create_time", "creator", "update_time", "updater", "system_code", "system_name"],
    "unique": [],
    "index": [],
    "default": {"role_code":None, "role_name":None, "user_id":None, "user_name":None, "create_time":"CURRENT_TIMESTAMP", "creator":None, "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "updater":None, "system_code":None, "system_name":None}
}

auth_sys_user = {
    "table_name": "auth_sys_user",
    "columns": ["id","sys_code", "sys_name", "user_id", "user_name", "create_time", "creator", "update_time", "updater"],
    "primary_key": ["id"],
    "nullable": ["user_id", "user_name", "create_time", "creator", "update_time", "updater"],
    "unique": [],
    "index": [],
    "default": {"user_id":None, "user_name":None, "create_time":"CURRENT_TIMESTAMP", "creator":None, "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "updater":None}
}

auth_system = {
    "table_name": "auth_system",
    "columns": ["code","name", "status", "remark", "create_time", "creator", "update_time", "updater"],
    "primary_key": ["code"],
    "nullable": ["status", "remark", "create_time", "creator", "update_time", "updater"],
    "unique": [],
    "index": [],
    "default": {"code":None, "name":None, "status":None, "remark":None, "create_time":"CURRENT_TIMESTAMP", "creator":None, "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "updater":None}
}

auth_unit = {
    "table_name": "auth_unit",
    "columns": ["id","auth_code", "auth_name", "unit_id", "unit_name", "create_time", "creator", "update_time", "updater", "system_code", "system_name"],
    "primary_key": ["id"],
    "nullable": ["unit_id", "unit_name", "create_time", "creator", "update_time", "updater", "system_code", "system_name"],
    "unique": [],
    "index": [],
    "default": {"unit_id":None, "unit_name":None, "create_time":"CURRENT_TIMESTAMP", "creator":None, "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP", "updater":None, "system_code":None, "system_name":None}
}

cc_blacklist = {
    "table_name": "cc_blacklist",
    "columns": ["id","number", "source", "remark", "status", "type", "free_time", "create_time", "update_time"],
    "primary_key": ["id"],
    "nullable": ["source", "remark", "status", "type", "free_time", "create_time", "update_time"],
    "unique": [],
    "index": [],
    "default": {"source":None, "remark":None, "status":None, "type":None, "free_time":None, "create_time":"CURRENT_TIMESTAMP", "update_time":"CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"}
}