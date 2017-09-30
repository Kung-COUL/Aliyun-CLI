#!/usr/bin/env python
# coding=utf-8
import stopEcs
import reinitDisk
import startEcs
import diaDescribeInstanceAttribute
import os
import time


stopEcs.doIt()

reinitDisk.doIt()

diaDescribeInstanceAttribute.status()

time.sleep(1)

startEcs.doIt()
