# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

from utils.notify import send_dingtalk_msg

def for_assertTrue(case, result={}):
    for k in result.keys():
        v = result[k]
        # print(" %s assert %s " % (k, v))
        try:
            assert v
        except Exception as e :
            reason = " %s obj assert false " % (k)
            msg = "EVCALL  Test Faild \nCase: "+case+ "\nReason: "+reason+""
            send_dingtalk_msg(msg)