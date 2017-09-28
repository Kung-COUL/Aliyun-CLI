# Aliyun-CLI<br />
<br />
<br />
每个文件夹是一个独立的服务器群脚本 &nbsp;<br />
<br />
<br />
pip install aliyun-python-sdk-core --target=lib<br />
pip install aliyun-python-sdk-ecs --target=lib<br />
<br />
<br />
Commented out lib/aliyunsdkcore/client.py line 184 to 187<br />
<br />
<br />
项目环境搭建<br />
1 安装python2.7.X(命令）<br />
<span style="white-space:pre">	</span>yum groupinstall -y 'development tools'<br />
<span style="white-space:pre">	</span>yum install -y zlib-devel bzip2-devel openssl-devel xz-libs wget<br />
<span style="white-space:pre">	</span>wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz<br />
<span style="white-space:pre">	</span>xz -d Python-2.7.8.tar.xz &nbsp;<br />
<span style="white-space:pre">	</span>tar -xvf Python-2.7.8.tar &nbsp;<br />
<span style="white-space:pre">	</span>cd Python-2.7.12<br />
<span style="white-space:pre">	</span>./configure --prefix=/usr/local<br />
<span style="white-space:pre">	</span>make &nbsp;<br />
&nbsp;<span style="white-space:pre">	</span>make altinstall<br />
&nbsp;<span style="white-space:pre">	</span>验证 python2.7 -V<br />
2 安装setuptools （命令）<br />
&nbsp;<span style="white-space:pre">	</span>2.1 wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-12.0.3.tar.gz#md5=f07e4b0f4c1c9368fcd980d888b29a65<br />
&nbsp;<span style="white-space:pre">	</span>2.2 tar -zxvf setuptools-12.0.3.tar.gz<br />
&nbsp;<span style="white-space:pre">	</span>2.3 cd setuptools=12.0.3<br />
&nbsp;<span style="white-space:pre">	</span>2.4 python setup.py install<br />
&nbsp;<span style="white-space:pre">	</span>2.5 验证是否安装成功 easy-install --help&nbsp;<br />
3 安装pip<br />
&nbsp; <span style="white-space:pre">	</span>curl https://bootstrap.pypa.io/get-pip.py | python2.7 -<br />
&nbsp;&nbsp;<br />
4 安装python环境依赖<br />
<span style="white-space:pre">	</span>yum install python-devel<br />
<br />
<br />
5 安装aliyun相关sdk(core 和ecs)<br />
&nbsp;<span style="white-space:pre">	</span>cd &nbsp; xx/xx/lib &nbsp;#切换至aliyunsdk存放目录<br />
&nbsp;<span style="white-space:pre">	</span>pip install aliyun-python-sdk-core --target=.<br />
&nbsp;<span style="white-space:pre">	</span>pip install aliyun-python-sdk-ecs --target=.<br />
&nbsp;<span style="white-space:pre">	</span>