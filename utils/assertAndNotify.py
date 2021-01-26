# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"

from utils.notify import send_dingtalk_msg

def assertAndNotify(code, valid, case, reason):
    '''
        code:实际返回的code
        valid:正确的code
        case:用例名称
        reason:报错原因（一般情况下是msg）
    '''
    try:
        assert code == valid
    except Exception as e:
        msg = "EVCALL  Test Faild \nCase: "+case+ "\nReason: "+reason+""
        send_dingtalk_msg(msg)
