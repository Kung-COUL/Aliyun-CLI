#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526 import CreateKeyPairRequest
import PropertiesUtils as p
import json
import os

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = CreateKeyPairRequest.CreateKeyPairRequest()
request.set_accept_format('json')

request.add_query_param('RegionId', p.regionId())
request.add_query_param('KeyPairName', p.keyPairName())

# 发起请求
response = clt.do_action(request)
print response

# 保存key
key = json.loads(response)["PrivateKeyBody"]
fp = open("ali.key","w")
fp.write(key)
fp.flush()
fp.close()


