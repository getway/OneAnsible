#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 下午5:06
# @Author  : xiaomao
# @File    : testurl.py

'''
测试一个URL返回是否正常放回
使用说明： ansible -i hosts all -m testurl -a "url='http://www.baidu.com' timeout=15"
'''

import urllib2
import re
from ansible.module_utils.basic import *

STATUS_200 = 0
STATUS_NOT_200 = 2
ERROR = 1
URL_ERROR = -1

#函数：获取url返回状态
def get_url_status(url, timeout=3):
    if not re.match(r'^https?:/{2}\w.+$', url):  
        return URL_ERROR, "URL Error: the url shoud be like http://%s"%url
    try:
        response = urllib2.urlopen(url, timeout = timeout)
        status = response.code
        if status == 200:
            return STATUS_200, "Status 200"
        else:
            return STATUS_NOT_200, "Not 200:%s"%status
    except Exception as e:
        return URL_ERROR, str(e)

#因为客户端有可能没有requests模块，所以直接使用urllib2    
# def get_url_status(url, timeout=3):
#     if not re.match(r'^https?:/{2}\w.+$', url):  
#         return URL_ERROR
#     try:
#         response = requests.get(url,timeout=timeout)
#         status = response.status_code
#         if response.status_code == requests.codes.ok:
#             return STATUS_200, "请求成功"
#         else:
#             return STATUS_NOT_200, "非200状态:%s"%status
#     except Exception as e:
#         return URL_ERROR, "网络错误..."


# 初始化一个module实例,传递进去的参数里面指定了url为必填项,用required=True修饰
module = AnsibleModule(
    argument_spec = dict(
        url=dict(required=True), 
        timeout=dict(required=False, type='int', default=3), 
        retry=dict(required=False, type='int', default=3),
    ),
    supports_check_mode=True
)

#在检测模式下不做具体操作，这个模块不会改变系统状态
if module.check_mode:
    module.exit_json(changed=False)

# 获取用户传递进来的name变量
url = module.params['url']
timeout = module.params['timeout']
retry = module.params['retry']

#请求5次，只要三次请求成功，则说明请求大致可以
n = 0
data = {'ok':None,'faild':None}
for i in range(0,retry):
    status, msg = get_url_status(url=url, timeout=timeout)
    if status == STATUS_200:
        n = n+1
        if not data['ok']:
            data['ok'] = [status, msg]
    else:
        if not data['faild']:
            data['faild'] = [status, msg]
if n==retry:
    status = data['ok'][0]
    msg = data['ok'][1]
    result = dict(msg=msg,rc=status)
    module.exit_json(**result)
else:
    status = data['faild'][0]
    msg = data['faild'][1]
    result = dict(msg=msg,rc=status)
    module.exit_json(**result)