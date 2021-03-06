# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import json
from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import DescribeInstanceAttributeRequest
import PropertiesUtils as p


def allAttributes():
    clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

    # 设置参数
    request = DescribeInstanceAttributeRequest.DescribeInstanceAttributeRequest()
    request.set_accept_format('json')

    request.add_query_param('InstanceId', p.instanceId())
    # 发起请求
    response = clt.do_action(request)

    # 输出结果
    # if __name__ == "__main__":
    # print json.dumps(json.loads(response), indent=2)

    print
    print json.loads(response)['InstanceName']
    print json.loads(response)['EipAddress']['IpAddress']
    print json.loads(response)['Status']
    print json.loads(response)['RegionId']
    print json.loads(response)['InstanceId']
    print json.loads(response)['ImageId']
    print


def status():
    clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

    # 设置参数
    request = DescribeInstanceAttributeRequest.DescribeInstanceAttributeRequest()
    request.set_accept_format('json')

    request.add_query_param('InstanceId', p.instanceId())
    # 发起请求
    response = clt.do_action(request)

    return json.loads(response)['Status']


if __name__ == "__main__":
    allAttributes()
