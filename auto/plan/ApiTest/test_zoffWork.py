#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、下班同时解绑车辆
'''
from auto.rescources.ApiTest.conf_api import off_work

from auto.rescources.ApiTest.conf_task_code import unit_dict

from utils.assertAndNotify import assertAndNotify

from time import sleep

def test_docOffWork(doctor_login_fix):

    hr, token, workstate = doctor_login_fix

    if workstate:        
        res = hr.request(off_work["method"], off_work["uri"])
        rj = res.json()
        assertAndNotify(rj["code"], 1, "test_docToWork", rj["msg"])
    else:
        pass
    sleep(3)
    
def test_driOffWork(driver_login_fix):

    hr, token, workstate = driver_login_fix

    if workstate:
        res = hr.request(off_work["method"], off_work["uri"])
        rj = res.json()
        assertAndNotify(rj["code"], 1, "test_driToWork", rj["msg"])
    else:
        pass
    sleep(3)

