#!/bin/bash

# Generate route-outgoing IP
function generateIp() {
    # set ip prefix
    ip_prefix="10.1.1."

    # get ip suffix
    line=$(ifconfig eth0 | head -n2 | tail -n1)
    reg="addr:([0-9\.]+)\s"
    [[ $line =~ $reg ]] && ip_suffix=$(echo ${BASH_REMATCH[1]} | awk -F'.' '{print $NF}')
    echo "${ip_prefix}${ip_suffix}"
}

outGoingIp=$(generateIp)

# echo $outGoingIp
#IFS="
#"
ifcfgTpl=$(cat << HEREDOC
DEVICE=eth0:0
ONBOOT=yes
BOOTPROTO=static
IPADDR=$outGoingIp
NETMASK=255.255.255.0
HEREDOC
)

echo "$ifcfgTpl"

# Setting ifcfg file
ifcfgFile="/etc/sysconfig/network-scripts/ifcfg-eth0:0"

echo "$ifcfgTpl" > $ifcfgFile

# Startup the  eth0:0
ifup eth0:0


# Delete the default gateway
oldDefaultGateway="${route -n | grep UGH | awk '{print $2}'}"
route del default gw ${oldDefaultGateway}

# Add new default gateway
newDefaultGateway="10.1.1.197"
route add default gw ${newDefaultGateway}
