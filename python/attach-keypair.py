
#coding=utf-8
#!/usr/bin/env python

from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526 import AttachKeyPairRequest
import PropertiesUtils as p
import json

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 奇怪的type转换，［］里面只能是str，不能是unicode
string = p.instanceId().encode('utf-8')
instanceId = [string]

# 设置参数
request = AttachKeyPairRequest.AttachKeyPairRequest()
request.set_accept_format('json')

request.add_query_param('RegionId', p.regionId())
request.add_query_param('KeyPairName', p.keyPairName())
request.add_query_param('InstanceIds', instanceId)

# 发起请求
response = clt.do_action(request)

# 输出结果
print json.dumps(json.loads(response), indent=2)
