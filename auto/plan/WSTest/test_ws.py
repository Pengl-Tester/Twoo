# # -*- coding:utf-8 -*-

# __author__ = "YuKwengRu"

# from time import sleep

# def test_ws(web_socket_connector):
#     l = [1,2,3]
#     for i in l:
#         wsc = web_socket_connector
#         ws = wsc.create_c("?uid=RYK&gid=JSFJ")
#         msg = "{\"from\":\"RYK\", \"to\":\"JSFJ\", \"body\":\"Hello\", \"type\":2}"
#         # msg = "123"
#         print(ws)
#         ws.send(msg)
#         print(i)
#         sleep(10)