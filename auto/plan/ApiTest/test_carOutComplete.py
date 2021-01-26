#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、医生或司机完成任务
'''
from auto.rescources.ApiTest.conf_api import accept, departure, arriveSite, returnHospital, arriveHospital, pending

from auto.rescources.ApiTest.conf_task_code import unit_dict

from utils.assertAndNotify import assertAndNotify

from time import sleep


def test_accept(doctor_login_fix):
    '''
        医生接受任务
    '''

    # hr, help_id, fist_dis_id = create_task_help_fix
    docHr, docToken, workState = doctor_login_fix

    res = docHr.request(accept["method"], accept["uri"])
    rj = res.json()
    print(rj)
    assertAndNotify(rj["code"], 1, "test_accept", rj["msg"])
    sleep(3)


def test_departure(driver_login_fix):
    '''
        司机离开现场
    '''

    # hr, help_id, fist_dis_id = create_task_help_fix
    driHr, driToken, workState = driver_login_fix

    res = driHr.request(departure["method"], departure["uri"])
    rj = res.json()
    print(rj)
    assertAndNotify(rj["code"], 1, "test_departure", rj["msg"])
    sleep(3)

def test_arriveSite(doctor_login_fix):

    '''
        医生到达现场
    '''
    # hr, help_id, first_dis_id = create_task_help_fix
    docHr, docToken, workState = doctor_login_fix

    res = docHr.request(arriveSite["method"], arriveSite["uri"])
    rj = res.json()
    print(rj)
    assertAndNotify(rj["code"], 1, "test_arriveSite", rj["msg"])
    sleep(3)


def test_returnHospital(driver_login_fix):
    '''
        司机返回医院
    '''
    # hr, help_id, first_dis_id = create_task_help_fix
    driHr, driToken, workState = driver_login_fix

    res = driHr.request(returnHospital["method"], returnHospital["uri"])
    rj = res.json()
    print(rj)
    assertAndNotify(rj["code"], 1, "test_returnHospital", rj["msg"])
    sleep(3)


def test_arriveHospital(doctor_login_fix):
    '''
        医生到达医院
    '''
    docHr, docToken, workState = doctor_login_fix

    res = docHr.request(arriveHospital["method"], arriveHospital["uri"])
    rj = res.json()
    print(rj)
    assertAndNotify(rj["code"], 1, "test_arriveHospital", rj["msg"])
    sleep(3)


def test_pending(driver_login_fix):
    '''
        司机站内待命
    '''
    driHr, driToken, workState = driver_login_fix

    res = driHr.request(pending["method"], pending["uri"])
    rj = res.json()
    print(rj)
    assertAndNotify(rj["code"], 1, "test_pending", rj["msg"])
    sleep(3)
