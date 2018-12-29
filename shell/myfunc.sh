#!/bin/bash

:<< COMMENTS
Author Cyril.Fung 2018.12.24
Check ALL the APPs 
     follow with IPs  one by one.
COMMENTS
set -e


#### Setup color functions for script
RESTORE=$(echo -en '\033[0m')
RED=$(echo -en '\033[00;31m')
GREEN=$(echo -en '\033[00;32m')
YELLOW=$(echo -en '\033[00;33m')
BLUE=$(echo -en '\033[00;34m')
MAGENTA=$(echo -en '\033[00;35m')
PURPLE=$(echo -en '\033[00;35m')
CYAN=$(echo -en '\033[00;36m')
LIGHTGRAY=$(echo -en '\033[00;37m')
LRED=$(echo -en '\033[01;31m')
LGREEN=$(echo -en '\033[01;32m')
LYELLOW=$(echo -en '\033[01;33m')
LBLUE=$(echo -en '\033[01;34m')
LMAGENTA=$(echo -en '\033[01;35m')
LPURPLE=$(echo -en '\033[01;35m')
LCYAN=$(echo -en '\033[01;36m')
WHITE=$(echo -en '\033[01;37m')

function echo_red() { local __text=$1; echo ${RED}${__text}${RESTORE}; }
function echo_yellow() { local __text=$1; echo ${YELLOS}${__text}${RESTORE}; }
function echo_cyan() { local __text=$1; echo ${CYAN}${__text}${RESTORE}; }
function echo_green() { local __text=$1; echo ${GREEN}${__text}${RESTORE}; }
function echo_magenta() { local __text=$1; echo ${MAGENTA}${__text}${RESTORE}; }
function echo_purple() { local __text=$1; echo ${PURPLE}${__text}${RESTORE}; }

function sleep_wait() { local __seconds=$1; sleep ${__seconds}; }

#### Setup output prefix  for script
OK="OK: Check "
WARNING="Warning: Check "
CRITICAL="Critical: Check "

function check_prog_install(){
    local __prog=$1; 
    command -v ${__prog} > /dev/null 2>&1 && echo 0 || echo 1
}

function check_url() {
    local __url=$1; 
    local __status_code=$(curl -I -m 5 -o /dev/null -s -w %{http_code} ${__url});
    echo ${__status_code};
}

function check_port {
    local __ip=$1;
    local __port=$2;
    /usr/bin/nc -zv -w 5 ${__ip} ${__port} > /dev/null 2>&1 && echo 0 || echo 1
}

function check_file_exists {
    local __file=$1;
    [[ -f "${__file}" ]]  > /dev/null 2>&1 && echo 0 || echo 1
}

function remote_check_file_exists {
   local __proc=$1;
   # For strings concat
   # sshpass -p 'pass' ssh -o StrictHostKeyChecking=no user@ip  "$(typeset -f check_file_exists);check_file_exists /tmp/myf.txt"
   echo '$(typeset -f check_file_exists);check_file_exists'
}

function check_dir_exists {
    local __dir=$1;
    [[ -d "${__dir}" ]]  > /dev/null 2>&1 && echo 0 || echo 1
}

function remote_check_dir_exists {
   local __proc=$1;
   # For strings concat
   echo '$(typeset -f check_dir_exists);check_dir_exists'
}

function check_proc_running {
   local __proc=$1;
   ps -C ${__proc} > /dev/null 2>&1 && echo 0 || echo 1
}

function remote_check_proc_running {
   local __proc=$1;
   # For strings concat
   # sshpass -p 'pass' ssh -o StrictHostKeyChecking=no user@ip  "$(typeset -f check_proc_running);check_proc_running zabbix_agent"
   echo '$(typeset -f check_proc_running);check_proc_running'
}
