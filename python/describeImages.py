
# coding=utf-8
#!/usr/bin/env python

from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import DescribeImagesRequest
import PropertiesUtils as p
import json

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = DescribeImagesRequest.DescribeImagesRequest()
request.set_accept_format('json')

# 发起请求
response = clt.do_action(request)

# 输出结果
images = json.loads(response)['Images']['Image']
totalCount = len(images)

for i in range(totalCount):
    print json.dumps(images[i]['ImageId'], indent=2)

print
