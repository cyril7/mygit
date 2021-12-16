#!/usr/bin/python
# -*- coding: UTF-8 -*-
#[root@me.com ~]# python -V
#Python 3.5.4
#name  check_port_open.py

import os,sys,socket

def usage():
    print """

ytmon_tools: Check a tcp|udp port is OPEN or CLOSED.
             The response code is always 0 while the TCP|UDP port is OPEN.

    Usage:
        python check_port_open.py [-h|--help] [tcp|udp] [ip] [port] [verbose]
    Options:
        --help|-h)
            Print help messages.
        udp|tcp)
            Specify the protocol
        ip)
            Specify the host address
        port)
            Specify port to check
        verbose)
            Specify to show more details
            
    Example:
        Check tcp port 
        input : python check_port_open.py  tcp  10.194.80.30 10080
        output: 11

        Check tcp port verbose
        input : python check_port_open.py  tcp  10.194.80.30 10080 vvv
        output: Res_code: 11, Protocol: tcp, IP: 10.194.80.30, Port: 10080 is "CLOSED".

        Check udp port
        input : python check_port_open.py udp 192.168.212.133 161
        output: 0

        Check udp port verbose
        input : python check_port_open.py udp 192.168.212.133 161 vvv
        output:Res_code: 0, Protocol: udp, IP: 192.168.212.133, Port: 161 is "OPEN".

"""

#socket try connect
def is_open(protocol, ip, port, verbose):
    protocol = protocol
    time_out = 3
    verbose  = verbose

    if protocol == 'udp':
        #s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        ''' send to /dev/null 2>&1 to suppress terminal output '''
        res = os.system("nc -vnzu -w "+ str(time_out) + " " + ip + " " + str(port) +" > /dev/null 2>&1")
        if res == 0:
            print( 'Res_code: %d, Protocol: %s, IP: %s, Port: %d is "OPEN".' %(res, protocol, ip, port) if verbose == 1 else (res))
        else:
            print( 'Res_code: %d, Protocol: %s, IP: %s, Port: %d is "CLOSED".' %(res, protocol, ip, port) if verbose == 1 else (res))
           

    elif protocol == 'tcp':
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.settimeout(time_out)
            #s.connect((ip,port))
            res = s.connect_ex((ip,port))
            s.settimeout(None)
            s.shutdown(2)
            #if res == 0 ... or not
            print( 'Res_code: %d, Protocol: %s, IP: %s, Port: %d is "OPEN".' %(res, protocol, ip, port) if verbose == 1 else (res))
        except:
            print( 'Res_code: %d, Protocol: %s, IP: %s, Port: %d is "CLOSED".' %(res, protocol, ip, port) if verbose == 1 else (res))

if __name__=='__main__':
    if len(sys.argv) == 1 or sys.argv[1] in ["-h","--h","-help","--help"]: 
        usage()
        sys.exit(3)
    else:
        protocol = sys.argv[1]
        ip       = sys.argv[2]
        port     = int(sys.argv[3])
        verbose  = 1  if len(sys.argv) > 4 else 0

        is_open(protocol, ip, port, verbose)

