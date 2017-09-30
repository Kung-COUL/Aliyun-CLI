#!/usr/bin/env python
# coding=utf-8

from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import StopInstanceRequest
import PropertiesUtils as p
import diaDescribeInstanceAttribute
import time
import json


def doIt():
    clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())
#    print type(p.accessKeyId())
#    print type( p.accessSecret())
#    print type(p.regionId())

    # 设置参数
    request = StopInstanceRequest.StopInstanceRequest()
    request.set_accept_format('json')
#    print type(p.instanceId())

    request.add_query_param('InstanceId', p.instanceId())

#    print type(request)
    # 发起请求
    response = clt.do_action_with_exception(request)

    # 输出结果
    print
    print json.loads(response)
    print "Stopping Server"

    i = 1
    while True:
        status = diaDescribeInstanceAttribute.status()

        if status != 'Stopped':
            print 'Stopping... ' + str(i)
            i += 1
            time.sleep(1)
        else:
            print 'Stopped'
            break


if __name__ == "__main__":
    doIt()
