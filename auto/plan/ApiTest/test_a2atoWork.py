#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、上班同时绑定车辆
'''
from auto.rescources.ApiTest.conf_api import to_work

from auto.rescources.ApiTest.conf_task_code import unit_dict

from utils.assertAndNotify import assertAndNotify

from time import sleep

def test_docToWork(doctor_login_fix):

    hr, token, workstate = doctor_login_fix
    
    if workstate:
        pass
    else:
        ambId = unit_dict["center"]["siteId"]["site1"]["ambId"][0]
        res = hr.request(to_work["method"], to_work["uri"])
        rj = res.json()
        assertAndNotify(rj["code"], 1, "test_docToWork", rj["msg"])
    sleep(3)
    

def test_driToWork(driver_login_fix):

    hr, token, workstate = driver_login_fix

    if workstate:
        pass
    else:
        ambId = unit_dict["center"]["siteId"]["site1"]["ambId"][0]
        res = hr.request(to_work["method"], to_work["uri"])
        rj = res.json()
        assertAndNotify(rj["code"], 1, "test_driToWork", rj["msg"])
    sleep(3)
    
