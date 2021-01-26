# -*- coding:utf-8 -*-

__author__ = "YukwengRu"

import json

import requests

from conf.configGlobal import DINGTALK_URL

# 发送钉钉文本通知
def send_dingtalk_msg(msg):
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text":{
            "content": msg
        },
        "at":{
            "atMobiles":[
                "18203017916"
            ],
            "isAtAll": "false"
        }
    }
    res=requests.post(DINGTALK_URL,data=json.dumps(data),headers=headers)