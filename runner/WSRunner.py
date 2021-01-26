# -*- coding:utf-8 -*-

__author__ = "yukwengru"

import websocket
from websocket import create_connection
from .runner import Runner

class WSRunner(Runner):
    def __init__(self, base_url="127.0.0.1", verify=False, headers = {}):
        super().__init__(name="WS Runner")
        self.base_url = base_url
        self.ws = websocket.WebSocket()
    
    def create_c(self, uri, **kwargs):
        url = self.base_url + uri
        try:
            self.ws = create_connection(url)
        except websocket.WebSocketException as e:
            print("WSRunner Exception: [%s]" % str(e))
        
        return self.ws
    
    def sen_msg(self, msg):
        self.ws.send(self, msg)