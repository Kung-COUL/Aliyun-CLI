Mou# Aliyun-CLI

每个文件夹是一个独立的服务器群脚本  

pip install aliyun-python-sdk-core --target=lib
pip install aliyun-python-sdk-ecs --target=lib

Commented out lib/aliyunsdkcore/client.py line 184 to 187

项目环境搭建
1 安装python2.7.X(命令）

    yum groupinstall -y 'development tools'
	yum install -y zlib-devel bzip2-devel openssl-devel xz-libs wget
	wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz
	xz -d Python-2.7.12.tar.xz  
	tar -xvf Python-2.7.12.tar  
	cd Python-2.7.12
	./configure --prefix=/usr/local
	make && make altinstall
 
 验证 python2.7 -V
 
2 安装setuptools （命令）

 	wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-12.0.3.tar.gz#md5=f07e4b0f4c1c9368fcd980d888b29a65
 	tar -zxvf setuptools-12.0.3.tar.gz
 	cd setuptools-12.0.3
 	python setup.py install
 
 验证是否安装成功 easy_install --help 
 
4 安装python环境依赖

	yum install python-devel

5 安装aliyun相关sdk(core 和ecs)

 	cd   xx/xx/lib  #切换至aliyunsdk存放目录
 	pip install aliyun-python-sdk-core --target=.
 	pip install aliyun-python-sdk-ecs --target=.
	
