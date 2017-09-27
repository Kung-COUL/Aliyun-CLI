# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import json
from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526 import DescribeInstanceAttributeRequest
import PropertiesUtils as p

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = DescribeInstanceAttributeRequest.DescribeInstanceAttributeRequest()
request.set_accept_format('json')

request.add_query_param('InstanceId', p.instanceId())
print request
# 发起请求
response = clt.do_action(request)

# 输出结果
print json.dumps(json.loads(response), indent=2)