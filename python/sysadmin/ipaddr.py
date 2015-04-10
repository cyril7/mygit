from IPy import IP

# 接受输入，参数为IP地址或者网段地址
ip_s = raw_input('Please input an IP or net-range: ')
ips = IP(ip_s)

# 为一个网络地址
if len(ips) > 1:
    # 输出网络地址
    print('net: %s' % ips.net())
    # 输出网络掩码地址
    print('netmask: %s' % ips.netmask())
    # 输出网络广播地址
    print('broadcast: %s' % ips.broadcast())
    # 输出地址反向解析
    print('reverse address: %s' % ips.reverseNames()[0])
    # 输出网络子网数
    print('subnet: %s' % len(ips))
    
# 为单个IP地址
else:
    # 输出地址反向解析
    print('reverse address: %s' % ips.reverseNames()[0])

# 输出16进制地址
print('hexadecimal: %s' % ips.strHex())
# 输出二进制地址
print('binary ip: %s' % ips.strBin())
# 输出地址类型,如PRIVATE, PUBLIC, LOOPBACK等
print('iptype: %s' % ips.iptype())
