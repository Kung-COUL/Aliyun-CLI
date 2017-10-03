
# coding=utf-8
#!/usr/bin/env python

from lib.aliyunsdkcore import client
from lib.aliyunsdkecs.request.v20140526 import ReInitDiskRequest
import PropertiesUtils as p
import json


def doIt():
    clt = client.AcsClient(p.accessKeyId(), p.accessSecret(), p.regionId())

    request = ReInitDiskRequest.ReInitDiskRequest()
    request.set_accept_format('json')

    request.add_query_param('DiskId', p.diskId())
    response = clt.do_action(request)

    print
    print json.loads(response)
    print "Server Reinitializing"


if __name__ == "__main__":
    doIt()
