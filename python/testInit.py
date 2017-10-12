#!/usr/bin/env python
# coding=utf-8
import stopEcs
import reinitDisk
import startEcs
import diaDescribeInstanceAttribute
import os
import time


#实际的效果命令由这边组合定义
stopEcs.doIt()

reinitDisk.doIt()

diaDescribeInstanceAttribute.status()

time.sleep(1)

startEcs.doIt()
