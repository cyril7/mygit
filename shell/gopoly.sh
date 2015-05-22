#!/bin/bash
ipList=$1
#polysh --hosts-file="$server_list" --password-file="pwd.txt" --ssh='ssh -l apps -p22 '
polysh --hosts-file="$ipList" --ssh='exec ssh -o StrictHostKeyChecking=no -p 22 -i /home/x/polyshfiles/.ssh/abc.private'
