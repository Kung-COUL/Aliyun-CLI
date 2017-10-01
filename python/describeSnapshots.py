
# coding=utf-8
#!/usr/bin/env python

from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import DescribeSnapshotsRequest
import PropertiesUtils as p
import json

clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

# 设置参数
request = DescribeSnapshotsRequest.DescribeSnapshotsRequest()
request.set_accept_format('json')

# 发起请求
response = clt.do_action(request)

# 输出结果
snapshots = json.loads(response)['Snapshots']['Snapshot']
totalCount = len(snapshots)

for i in range(totalCount):
    # print
    print json.dumps(snapshots[i]['SnapshotName'])
    # print json.dumps(snapshots[i]['SnapshotId'])
    # print json.dumps(snapshots[i]['SourceDiskId'])
    # print

# print json.dumps(json.loads(response), indent=2)
