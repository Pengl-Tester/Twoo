__author__ = "YuKwengRu"

import pytest

from runner.DBRunner import DBRunner

from auto.rescources.DatabaseTest.conf_db import EV_CALL_01

from utils.myassert import for_assertTrue

from utils.notify import send_dingtalk_msg

def test_evcall01_tables(database_connector):

    for_assertTrue(database_connector.has_tables(EV_CALL_01["tables"]))

    send_dingtalk_msg("服务监控123")