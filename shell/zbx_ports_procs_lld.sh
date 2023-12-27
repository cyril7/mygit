#!/bin/bash

: <<'END_COMMENT'
exclude="zabbix_agentd|monit|snmpd|sendmail|moxi|java|ceph-osd"
conf="/etc/etc_zbx_procs_ports_lld.conf"
common="sshd|dnsmasq|agentd_zbx"
kubecommon="$common|10248:kubelet|10249:kube-proxy|10250:kubelet|10256:kube-proxy|179:bird|9099:calico-node"

hostname | grep "k8s-master" &>/dev/null && r=0 || r=1
[ $r -eq 0 ] && include="$kubecommon|10251:kube-scheduler|10252:kube-controller|2379:etcd|2380:etcd|443:kube-apiserver"

hostname | grep "k8s-etcd" &>/dev/null && r=0 || r=1
[ $r -eq 0 ] && include="$kubecommon|2379:etcd|2380:etcd"

hostname | grep "k8s-router" &>/dev/null && r=0 || r=1
[ $r -eq 0 ] && include="$kubecommon|80:nginx|443:nginx"

hostname | grep "k8s-node" &>/dev/null && r=0 || r=1
[ $r -eq 0 ] && include="$kubecommon"

if [ -f $conf ];then
    source $conf
fi

function ntlp()
{
    sudo timeout 5 ss -ltpn |awk '{print $4,$6}' |sed 's/::ffff://g' |perl -pe 's/.*?:(\d)/\1/' |sed 's/users:((\"//g'|sed 's/\".*$//' |grep -vE "127.0.0.1|172.17.|Local" |sort -u |grep -v ":" |tr ' ' ':' | grep -v ":$"
}
END_COMMENT

# Return the value
str='{\n\t"data":['
confstr=""

case "$1" in
    ports)
        include="10050:zabbix_agentd|22:sshd|"    
        if [ "$include"x != ""x ];then
            for id in `echo $include |tr '|' ' '`;do
                proc=`echo $id | cut -f2 -d':'`
                port=`echo $id | cut -f1 -d':'`
                str="$str\n\t\t{\"{#PROCNAME}\":\"$proc\", \"{#PORT}\":\"$port\"},"
                confstr="$confstr|$port:$proc"
            done
        else
            echo "请按端口:进程名称格式填写变量"'$include'
            echo '-- include="10050:zabbix_agentd|22:sshd|"'
        fi
    ;;
    procs)
        include="zabbix_agentd|sshd|"    
        if [ "$include"x != ""x ];then
            for id in `echo $include |tr '|' ' '`;do
                proc=`echo $id | cut -f2 -d':'`
                #str="$str\n\t\t{\"{#PROC_COUNT}\":\"$proc\", \"{#PORT}\":\"$port\"},"
                str="$str\n\t\t{\"{#PROC_COUNT}\":\"$proc\","
                confstr="$confstr|$proc"
            done
        else
            echo "请按进程名称格式填写变量"'$include'
            echo '-- include="zabbix_agentd|sshd|"'
        fi
    ;;
    *)
        echo "USAGE: $0 ports|procs"
        #echo -e $str || echo $confstr |sed 's/^|//g'
        exit 1;
    ;;
esac

str="$str]\n}"
str=`echo $str |sed 's/,]/\\\\n\\\\t]/g'`
#[ $# -lt 1 ] && echo -e $str || echo $confstr |sed 's/^|//g'
[ $# -ge 1 ] && echo -e $str || echo $confstr |sed 's/^|//g'
