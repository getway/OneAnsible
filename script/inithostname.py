#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  生成一个12位的ip地址
"""
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def get_full_ip(ifname):
    ip = get_ip_address(ifname)
    iponly = ''.join([i.zfill(3) for i in ip.split('.')])
    return iponly

if __name__ == "__main__":
    ifname = "eth1"
    print(get_full_ip(ifname))