
#coding=utf-8
#!/usr/bin/env python

from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526 import AssociateEipAddressRequest
import PropertiesUtils as p
import json

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = AssociateEipAddressRequest.AssociateEipAddressRequest()
request.set_accept_format('json')

request.add_query_param('InstanceId', p.instanceId())
request.add_query_param('AllocationId', p.allocationId())

# 发起请求
response = clt.do_action(request)

# 输出结果
print json.dumps(json.loads(response), indent=2)
