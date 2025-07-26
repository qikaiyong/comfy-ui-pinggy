#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-05-02 19:56
# @Author  : 我的名字
# @File    : __init__.py
# @Description : 这个函数是用来balabalabala自己写
import pinggy

# Start an HTTP tunnel forwarding traffic to localhost on port 8000
tunnel = pinggy.start_tunnel(forwardto="localhost:8188", token="PQiHccJpcr4")
print(f"Tunnel started. Urls: {tunnel.urls}")

