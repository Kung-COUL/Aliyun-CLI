#coding=utf-8
#!/usr/bin/env python

from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526 import StartInstanceRequest
import PropertiesUtils as p

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = StartInstanceRequest.StartInstanceRequest()
request.set_accept_format('json')

request.add_query_param('InstanceId', p.instanceId())

# 发起请求
response = clt.do_action_with_exception(request)

# 输出结果
print response