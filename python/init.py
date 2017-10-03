#!/usr/bin/env python
# coding=utf-8
import stopEcs
import reinitDisk
import startEcs
import time


stopEcs.doIt()

time.sleep(2)

reinitDisk.doIt()

time.sleep(2)

startEcs.doIt()
