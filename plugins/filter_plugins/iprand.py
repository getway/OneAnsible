#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  生成一个12位的ip地址
"""

def iprand(ip):
    iprand = ''.join([i.zfill(3) for i in ip.split('.')])
    return iprand

class FilterModule(object):
    def filters(self):
        return {'iprand':iprand}