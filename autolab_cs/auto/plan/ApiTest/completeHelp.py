#  -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

'''
    1、查询当前中心坐席下所有任务
    2、中心取消所有任务
'''

from auto.rescources.ApiTest.conf import complete

from utils.assertAndNotify import assertAndNotify

def test_complete(create_task_help_fix):
    '''
        坐席完成求救任务
    '''

    hr, help_id, first_dispatch_id = create_task_help_fix
    print(help_id)
    print(first_dispatch_id)
    res = hr.request(complete["method"], complete["uri"], params = {"dispatchId": first_dispatch_id})
    rj = res.json()
    assertAndNotify(rj["code"], 1, "test_complete", rj["msg"])