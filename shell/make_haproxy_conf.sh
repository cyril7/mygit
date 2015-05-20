#!/bin/bash

IFS="
"

TAG=$(cat << 'HEREDOC'
HZ5-xyz-013	10.1.1.155
HZ5-xyz-014	10.1.1.156
HZ5-xyz-015	10.1.1.157
HZ5-xyz-016	10.1.1.158
HZ5-xyz-017	10.1.1.159
HZ5-xyz-018	10.1.1.160
HZ5-xyz-019	10.1.1.161
HZ5-xyz-020	10.1.1.162
HEREDOC
)

for line in $(echo "$TAG")
do
    hostname=$(echo $line | awk '{print $1}')
    ip=$(echo $line | awk '{print $2}')
    echo "        server  $hostname ${ip}:80 cookie $hostname check inter 2000 rise 3 fall 3 weight 20"
done
