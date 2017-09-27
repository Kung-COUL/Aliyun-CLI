#!/usr/bin/python
# -*- coding:utf-8 -*-
###################################
#
# 检查主机的损坏磁盘
#
###################################
 
import paramiko
import sys
import PropertiesUtils as p


def sshConnect(ip):
    try:
        # 建立一个sshclient对象
        ssh = paramiko.SSHClient()
        # 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数
        # pkey = paramiko.RSAKey.from_private_key_file('/home/super/.ssh/id_rsa', password='12345')
        pkey = paramiko.RSAKey.from_private_key_file('ali.key')
        # 建立连接
        ssh.connect(hostname=ip,
                    port=22,
                    username='root',
                    pkey=pkey)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command("systemctl restart httpd")
        # 结果放到stdout中，如果有错误将放到stderr中
        print(stdout.read().decode())
        print(stderr.read())
        # 关闭连接
        ssh.close()
    except Exception,e:
        print e

sshConnect('47.52.139.152')
