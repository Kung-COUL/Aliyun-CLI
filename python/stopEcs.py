#!/usr/bin/env python
# coding=utf-8

from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import StopInstanceRequest
import PropertiesUtils as p


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
    if __name__ == "__main__":
        print response


if __name__ == "__main__":
    doIt()
