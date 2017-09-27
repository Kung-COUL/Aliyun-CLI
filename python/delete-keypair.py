
#coding=utf-8
#!/usr/bin/env python

from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526 import DescribeKeyPairsRequest
import PropertiesUtils as p
import json

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = DeleteKeyPairsRequest.DeleteKeyPairsRequest()
request.set_accept_format('json')

request.add_query_param('RegionId', 'cn-hongkong')
request.add_query_param('KeyPairNames', 'Kung')

# 发起请求
response = clt.do_action(request)

# 输出结果
print json.dumps(json.loads(response), indent=2)
