#!/usr/bin/python
# by criver

import socket
import time
import sys
import signal
import subprocess
import fcntl  
import struct 

def stats(host,port):
        #host='127.0.0.1'
        #port=11211
        result = ''
        try:
                # 打开SOCKET
                sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                sk.settimeout(1)
                sk.connect((host,port))
                cmd='stats\r\n'
                sk.send(cmd)
                result=sk.recv(4096)
                sk.close()
        except socket.error,ex:
                print '[EX][stats] %s'%str(ex)
        #print result
        st = extract(result) 
        return st

def extract(result):
        # 结果通过换行符分割
        result_ar = result.split("\r\n")
        status = {}
        for ar in result_ar:
                if (ar!='END') and (ar!=''):
                        sp = ar.split()
                        status[sp[1]]=sp[2]
        output = process(status)
        return output 

def process(status):
        out = {}
        out['in']  = int(status['bytes_read'])
        out['out'] = int(status['bytes_written'])
        return out

def human_format(num):
        if num > 1073741824 :
                return '%.2f' % (num/1073741824.0) + 'G'
        elif num > 1048576 :
                return '%.2f' % (num/1048576.0) + 'M'
        elif num > 1024 :
                return '%.2f' % (num/1024.0) + 'K'
        else:
                return '%d' % num + 'B'
        return 

def signal_handler(signal,frame):
        print '\n'
        sys.exit(0)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, # SIOCGIFADDR  
        struct.pack('256s', ifname[:15])
    )[20:24])

def discovery_mc() :
    pp  = subprocess.Popen("ss -4nlp | grep -E 'mysqld|redis-server|memcached' | awk '{print $3}' |awk -F':' '{print $2}'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    ports = pp.communicate()[0].strip()
    #print ports 
    return ports
        
def get_all_stats(ip,ports) :
        sts = {}
        for p in ports :
                st = stats(ip,int(p))
                io = [st['in'],st['out']]
                sts[p] = io
        return sts

def main():
        ports = discovery_mc().split('\n')
        ip = get_ip_address('bond0')
        last_status = get_all_stats(ip,ports)

        title ={}
        title['time'] ='--------------------'
        title['ip']  = '------ip--------'
        title['port'] = '---port---' 
        title['in'] = '---in---' 
        title['out'] = '---out---' 
        title['total'] = '---total---' 
        tt = ['time','ip','port','in','out','total']

        timf  = '{0:>%s}'%(len(title['time']))
        ipf = '{0:>%s}'%(len(title['ip']))
        portf = '{0:>%d}'%(len(title['port']))
        inf = '{0:>%s}'%(len(title['in']))
        outf = '{0:>%s}'%(len(title['out']))
        totalf = '{0:>%s}'%(len(title['total']))


        t_value = '|'
        for t in tt :
                 t_value  += title[t] + "|"

        while 1:
                #print "%s%s%s%s%s%s" %(title['ip'],title['port'],title['in'],title['out'],title['total']) 
                time.sleep(0.99)
                status = get_all_stats(ip,ports)
                print  t_value
                tim = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))

                for p in ports :
                        str_value = '|'
                        #print "%s"p , status[p][0]-last_status[p][0],status[p][1]-last_status[p][1]
                        inb  = status[p][0]-last_status[p][0]
                        outb = status[p][1]-last_status[p][1]
                        totalb = inb + outb
                        str_value += timf.format(tim) + "|" + ipf.format(ip) +"|"+  portf.format(p) + "|" + inf.format(human_format(inb)) + "|" \
                                + outf.format(human_format(outb)) + "|" + totalf.format(human_format(totalb)) + "|"
                        print str_value

                last_status = status

main()
