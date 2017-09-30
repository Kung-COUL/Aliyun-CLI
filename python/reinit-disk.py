
# coding=utf-8
#!/usr/bin/env python

from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import ReInitDiskRequest
import PropertiesUtils as p
import json

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = ReInitDiskRequest.ReInitDiskRequest()
request.set_accept_format('json')

request.add_query_param('DiskId', p.diskId())


# 发起请求
response = clt.do_action(request)

# 输出结果
print json.dumps(json.loads(response), indent=2)
