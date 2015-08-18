#!/bin/bash

#################################
## geotrace是根据mtr（my trace route）的报告内容结合whois来直观显示traceroute过程中
## 经过的路由跳数、ip、平均延迟、运营商、地理位置信息等内容，在做
## 机房选址的时候会给带来极大的帮助，报告内容一目了然。
## 运行系统：linux/macos
## 依赖程序：mtr、whois、awk
## 使用方法：
## 1、确保依赖程序正常；
## 2、wget https://raw.githubusercontent.com/LaiJingli/geotrace/master/geotrace.sh
## chmod +x geotrace.sh
## ./geotrace.sh ip/domai

#################################

echo traceroute to [$1] from localhost
ip=$1
echo

####如果是linux系统请将mac部分注释掉，反之亦然

####for linux
####显示详细地理位置信息
#echo ----显示详细地理位置信息----
#mtr --n --report $ip|grep -v Snt|awk '{printf "%-18s  %-10s",  NR ") "$1,"  Delay["$4"s]   ";system("whois "$1"|grep -e netname -e descr|cut -c17-");printf "\n"}'
####显示简略地理位置信息
#echo ----显示简略地理位置信息---
#mtr --n --report $ip|grep -v Snt|awk '{printf "%-18s  %-10s",  NR ") "$1,"  Delay["$4"s]   ";system("whois "$1"|grep descr|head -n1|cut -c17-");printf "\n"}'


###for mac
####显示详细地理位置信息
echo ----显示详细地理位置信息----
mtr --n --report $ip|grep -vE "Snt|Start"|awk '{printf "%-18s  %-10s",  NR ") "$2, " Dleay["$6"]  ";system("whois "$2"|grep -e netname -e descr|cut -c17-");printf "\n"}'
####显示简略地理位置信息
echo ----显示简略地理位置信息---
mtr --n --report $ip|grep -vE "Snt|Start"|awk '{printf "%-18s  %-10s",  NR ") "$2, " Dleay["$6"]  ";system("whois "$2"|grep descr|head -n1|cut -c17-");printf "\n"}'
