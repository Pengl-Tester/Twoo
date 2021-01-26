# -*- coding:utf-8 -*-

__author__ = "YukwengRu"

"""
    全局变量&&通用配置
"""
# JENKINS钉钉机器人ID
# JENKINS_DINGTALK_TOKEN = "a0aed95d-d00a-4210-b78c-62dee56a7e0f"

# 钉钉群机器人token(PROD环境)
DINGTALK_URL = "https://oapi.dingtalk.com/robot/send?access_token=54aafab7ced6382e2e37f3132f0fb78153078bdfe6a7854aa1c7b6fa45f5f385"

# 数据库连接配置
# PROD
# DBURL = "mysql+pymysql://jsfj_role:jsfj@120JSFJ@47.106.21.209:3306/ev-call-01"
# 天翼云
DBURL = "mysql+pymysql://root:jsfj120JSFJ!@#@219.151.148.184:63306/ev-call-01"

# SIT
# VALIDDBURL = "mysql+pymysql://root:jsfj120JSFJ!@)@192.168.2.230:3306/ev-call-01"
# PROD
VALIDDBURL = "mysql+pymysql://jsfj_role:jsfj@120JSFJ@47.106.21.209:3306/ev-call-01"


# DEV
# URL = "mysql+pymysql://jsfj_role:jsfj120JSFJ@192.168.0.87:3306/ev-call-01"

# web服务连接配置
HTTPURL = "https://www.jshi9.com/4.0api"

# WS连接
WSURL = "ws://192.168.0.94:18091"