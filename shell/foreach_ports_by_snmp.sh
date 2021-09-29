#!/usr/bin/env bash 

### By fengzhichao 2021.09.27
### foreach_ports_by_snmp.sh 
###   -- Foreach netdev ports by snmpwalk.
###   -- Redirect the output to a file.
###
### Usage:
###   bash foreach_ports_by_snmp.sh 2c 'abcdefg' 192.168.210.10
###
### Options:
###   <$1>           Snmp version.
###   <$2>           Snmp community strings with 'single quotes'.
###   <$3>           Net device IP address.
###   -h | --help    Show this message.

help() {
    sed -rn 's/^### ?//;T;p;' "$0"
}

if [[ $# == 0 ]] || [[ $# != 3 ]] || [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]; then
	    help
	    exit 1
fi

snmpversion=$1
snmpcommunity=$2
targetip=$3
logfile="${targetip}_ports_snmpdetail.txt"

#### Man rm:
#### To remove a file whose name starts with a '-', for example '-foo',
#### use one of these commands:
####  rm -- -foo
####  rm ./-foo
[ -e ${logfile} ] && rm -f -- ${logfile}


alias_pattern1='STRING: H[1-9]' 
alias_pattern2='STRING: [L|l]ink[-|_]'
alias_pattern3='STRING: [T|t][-|_]'
concat_alias_pattern="${alias_pattern1}|${alias_pattern2}|${alias_pattern3}"

incorrect_alias_ifindex=$(snmpwalk -v ${snmpversion} -c ${snmpcommunity} ${targetip} IF-MIB::ifAlias  | grep -vE "${concat_alias_pattern}"  | cut -d ' ' -f1 | cut -d '.' -f2 | xargs)
#echo ${incorrect_alias_ifindex}

printf "==== %-100s ====\n" "Incorrect Alias" | tee -a ${targetip}_ports_snmpdetail.txt 2>&1
printf "%-8s | %-60s | %-40s | %-10s\n" "ifIndex" "ifAlias" "ifDescr" "ifOperStatus" | tee -a ${targetip}_ports_snmpdetail.txt 2>&1

for ifindex in ${incorrect_alias_ifindex}
do
    ifalias=$(snmpwalk -v ${snmpversion} -c ${snmpcommunity} ${targetip} IF-MIB::ifAlias.${ifindex} | awk -F' ' '{print $NF}')
    ifdescr=$(snmpwalk -v ${snmpversion} -c ${snmpcommunity} ${targetip} IF-MIB::ifDescr.${ifindex} | awk -F' ' '{print $NF}')
    ifoperstatus=$(snmpwalk -v ${snmpversion} -c ${snmpcommunity} ${targetip} IF-MIB::ifOperStatus.${ifindex} | awk -F' ' '{print $NF}')
    printf "%-8s | %-60s | %-40s | %-10s\n" "${ifindex}" "${ifalias}" "${ifdescr}" "${ifoperstatus}"
    sleep 1
done | tee -a ${targetip}_ports_snmpdetail.txt 2>&1

echo 
echo

correct_alias_ifindex=$(snmpwalk -v ${snmpversion} -c ${snmpcommunity} ${targetip} IF-MIB::ifAlias  | grep -E "${concat_alias_pattern}"  | cut -d ' ' -f1 | cut -d '.' -f2 | xargs)
#echo ${correct_alias_ifindex}

printf "==== %-100s ====\n" "Correct Alias" | tee -a ${targetip}_ports_snmpdetail.txt 2>&1
printf "%-8s | %-60s | %-40s | %-10s\n" "ifIndex" "ifAlias" "ifDescr" "ifOperStatus" | tee -a ${targetip}_ports_snmpdetail.txt 2>&1

for ifindex in ${correct_alias_ifindex}
do
    ifalias=$(snmpwalk -v ${snmpversion} -c ${snmpcommunity} ${targetip} IF-MIB::ifAlias.${ifindex} | awk -F' ' '{print $NF}')
    ifdescr=$(snmpwalk -v ${snmpversion} -c ${snmpcommunity} ${targetip} IF-MIB::ifDescr.${ifindex} | awk -F' ' '{print $NF}')
    ifoperstatus=$(snmpwalk -v ${snmpversion} -c ${snmpcommunity} ${targetip} IF-MIB::ifOperStatus.${ifindex} | awk -F' ' '{print $NF}')
    printf "%-8s | %-60s | %-40s | %-10s\n" "${ifindex}" "${ifalias}" "${ifdescr}" "${ifoperstatus}"
    sleep 1
done | tee -a ${targetip}_ports_snmpdetail.txt 2>&1
