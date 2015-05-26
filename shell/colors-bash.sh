#!/bin/bash 
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

# Test
echo ${RED}RED${GREEN}GREEN${YELLOW}YELLOW${BLUE}BLUE${PURPLE}PURPLE${CYAN}CYAN${WHITE}WHITE${RESTORE} RESTORE


function echo_red() { local __text=$1; echo ${RED}${__text}${RESTORE}; }
function echo_yellow() { local __text=$1; echo ${YELLOS}${__text}${RESTORE}; }
function echo_cyan() { local __text=$1; echo ${CYAN}${__text}${RESTORE}; }
function echo_green() { local __text=$1; echo ${GREEN}${__text}${RESTORE}; }
function echo_blue() { local __text=$1; echo ${BLUE}${__text}${RESTORE}; }
function echo_magenta() { local __text=$1; echo ${MAGENTA}${__text}${RESTORE}; }
function echo_purple() { local __text=$1; echo ${PURPLE}${__text}${RESTORE}; }


txt='aaa'
echo_red $txt
echo_yellow $txt
echo_cyan $txt
echo_green $txt
echo_blue $txt
echo_magenta $txt
echo_purple $txt
