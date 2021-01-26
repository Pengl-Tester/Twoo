# -*- coding: utf-8 -*-

__author__ = "YuKwengRu"



# for http
import re
import requests
from requests import Request
from requests.auth import HTTPBasicAuth

from .runner import Runner

class HttpRunner(Runner):
    def __init__(self, base_url="127.0.0.1", verify=False, headers = {}):
        super().__init__(name="Http Runner")
        self.base_url = base_url
        self.http = requests.Session()

        # 在session实例上挂载Adapter实例， 目的：请求异常时，自动重试
        a = requests.adapters.HTTPAdapter(max_retries=3)
        self.http.mount('http://', a)
        self.http.verify = verify
        self.http.headers = headers
        self.token="" # 登录token

        self.r = None

    def auth(self, uri, user, passwd):
        url = self.base_url + uri

        return self.http.get(url, auth=HTTPBasicAuth(user, passwd))
    
    def request(self, method, uri, **kwargs):
        """
            该函数参数与requests库的request方法
            method： GET、POST、DELETE、PUT HEADER等等
            uri: 目标请求资源
            kwargs: 其他请求参数
            返回requests Response 对象
            **kwargs
        """
        url = self.base_url + uri
        try:
            self.r = self.http.request(method=method, url=url, **kwargs)
        except requests.exceptions.ConnectTimeout as e:
            print("HttpRunner Exception: [%s]" % str(e))
        except requests.exceptions.InvalidURL as e:
            print("Http Runner Exception: [%s]" % str(e))
        
        return self.r
    
    @property
    def status_code(self):
        """
            获取http相应状态码
        """

        return self.r.status_code

    @property
    def encoding(self):
        """
            获取http相应内容coding
        """

        return self.r.coding

    def get_headers(self, key=None):
        """
            获取http响应headers, dict类型
        """
        if key is None:
            return self.r.headers
        else:
            return self.r.headers[key]
    
    @property
    def json(self):
        """
            获取json格式的响应内容
        """

        return self.r.json()
    
    @property
    def text(self):
        """
            获取原始响应内容
        """

        return self.r.text
    
    def get_http(self):
        """
            返回requests.session对象，用于直接操作requests
        """

        return self.http
    
    def close(self):
        """
            断开http连接
        """

        self.http.close()    
