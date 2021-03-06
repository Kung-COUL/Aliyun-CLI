
# coding=utf-8
#!/usr/bin/env python

from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
import PropertiesUtils as p
import json

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_accept_format('json')

request.add_query_param('RegionId', p.regionId())

# 发起请求
response = clt.do_action(request)

# 输出结果
# print json.dumps(json.loads(response), indent=2)

totalCount = json.loads(response)['TotalCount']

for i in range(totalCount):
    try:
        print 'Eip: ' + json.loads(response)['Instances']['Instance'][i]['EipAddress']['IpAddress']
        print 'PublicIp: ' + json.loads(response)['Instances']['Instance'][i]['PublicIpAddress']['IpAddress'][0]
        print 'Status: ' + json.loads(response)['Instances']['Instance'][i]['Status']
        print
    except IndexError:
        print 'an index error'
        print
