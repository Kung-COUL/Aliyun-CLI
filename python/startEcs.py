# coding=utf-8
#!/usr/bin/env python

from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import StartInstanceRequest
import PropertiesUtils as p
import os
import time
import json


def doIt():
    clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

    # 设置参数
    request = StartInstanceRequest.StartInstanceRequest()
    request.set_accept_format('json')

    request.add_query_param('InstanceId', p.instanceId())

    # 发起请求
    response = clt.do_action_with_exception(request)

    # 输出结果
    print
    print json.loads(response)
    print "Starting Server"

    pingTarget = p.pingTarget()

    i = 1
    while True:
        response = os.system("ping -c 1 -W 1 " +
                             pingTarget + ' >/dev/null')
        if response == 0:
            print 'Ready for ssh'
            break
        else:
            print "Starting... " + str(i)
            i += 1
            time.sleep(0.5)


if __name__ == "__main__":
    doIt()
