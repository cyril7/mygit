#!/bin/bash

:<< COMMENTS
Exit immediately if a simple command (see Section 3.2.1 [Simple
    Commands], page 8) exits with a non-zero status, unless the command
    that fails is part of the command list immediately following
    a while or until keyword, part of the test in an if statement,
    part of a && or || list, or if the command’s return status is being
    inverted using !. A trap on ERR, if set, is executed before the shell
    exits.
COMMENTS
set -e


## install epel base on /etc/issue
# CentOS and Red Hat Enterprise Linux 5.x
rpm -ivh http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
# CentOS and Red Hat Enterprise Linux 6.x
#rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
# CentOS and Red Hat Enterprise Linux 7.x
#rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
sed -i 's/https:/http:/g' /etc/yum.repos.d/epel*  

# install zlib
yum install -y zlib zlib-devel

## define PATH
TARBALL_DOWNLOAD_PATH="/tmp"
PY_INSTALL_PATH="/usr/local/python-2.7.3"

## install python 2.7.3
wget -O ${TARBALL_DOWNLOAD_PATH}/Python-2.7.3.tar.bz2  https://www.python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2
cd ${TARBALL_DOWNLOAD_PATH}
tar jxvf Python-2.7.3.tar.bz2
cd ${TARBALL_DOWNLOAD_PATH}/Python-2.7.3
./configure --prefix=${PY_INSTALL_PATH} && make && make install
ln -s  ${PY_INSTALL_PATH}/bin/python /usr/bin/python2.7.3

## install setuptools 0.6c11
wget -O ${TARBALL_DOWNLOAD_PATH}/setuptools-0.6c11.tar.gz  http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz --no-check-certificate
cd ${TARBALL_DOWNLOAD_PATH}
tar zxvf setuptools-0.6c11.tar.gz
cd ${TARBALL_DOWNLOAD_PATH}/setuptools-0.6c11
${PY_INSTALL_PATH}/bin/python setup.py build && ${PY_INSTALL_PATH}/bin/python setup.py install

## install pip 1.1
wget -O ${TARBALL_DOWNLOAD_PATH}/pip-1.1.tar.gz --no-check-certificate http://pypi.python.org/packages/source/p/pip/pip-1.1.tar.gz
cd ${TARBALL_DOWNLOAD_PATH}
tar zxvf pip-1.1.tar.gz
cd ${TARBALL_DOWNLOAD_PATH}/pip-1.1
${PY_INSTALL_PATH}/bin/python setup.py build && ${PY_INSTALL_PATH}/bin/python setup.py install
ln -s  ${PY_INSTALL_PATH}/bin/pip /usr/bin/pip2.7

# edit pip conf
cd /root/ && mkdir -p .pip
touch /root/.pip/pip.conf
TAG=$(cat << 'EOF' 
[global]
timeout = 2000
index-url = http://pypi.mirrors.ustc.edu.cn/simple
[install]
use-mirrors = true
mirrors = http://pypi.mirrors.ustc.edu.cn
EOF
)
echo "$TAG" > /root/.pip/pip.conf
# verify install result
pip2.7 search django
