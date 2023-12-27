#!/bin/bash
exclude="zabbix_agentd|monit|snmpd|sendmail|moxi|[0-9]{4,5}:java|ceph-osd|22"
conf="/etc/etc_zbx_ports_lld.conf"

common="22:sshd|53:dnsmasq|10040:agentd_zx"
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

str='{\n\t"data":['
confstr=""

function ntlp()
{
        sudo timeout 5 ss -ltpn |awk '{print $4,$6}' |sed 's/::ffff://g' |perl -pe 's/.*?:(\d)/\1/' |sed 's/users:((\"//g'|sed 's/\".*$//' |grep -vE "127.0.0.1|172.17.|Local" |sort -u |grep -v ":" |tr ' ' ':' | grep -v ":$"
}

if [ "$include"x != ""x ];then
        for id in `echo $include |tr '|' ' '`;do
            proc=`echo $id | cut -f2 -d':'`
            port=`echo $id | cut -f1 -d':'`
            str="$str\n\t\t{\"{#PROCNAME}\":\"$proc\", \"{#PORT}\":\"$port\"},"
            confstr="$confstr|$port:$proc"
        done
else
        for id in `ntlp |grep -vEw "$exclude"`;do
            proc=`echo $id | cut -f2 -d':'`
            port=`echo $id | cut -f1 -d':'`
            str="$str\n\t\t{\"{#PROCNAME}\":\"$proc\", \"{#PORT}\":\"$port\"},"
            confstr="$confstr|$port:$proc"
        done
fi
str="$str]\n}"
str=`echo $str |sed 's/,]/\\\\n\\\\t]/g'`
[ $# -lt 1 ] && echo -e $str || echo $confstr |sed 's/^|//g'
