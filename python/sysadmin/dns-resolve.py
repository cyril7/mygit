#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dns.resolver

domain = raw_input('Please input an domain: ')

# 查询A记录
A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        print j.address
        #print j
        
# 查询MX记录
MX = dns.resolver.query(domain, 'MX')
for i in MX:
    print 'MX preference =', i.preference, 'mail exchanger =', i.exchange
    
# 查询NS记录，只限一级域名, 比如baidu.com
ns = dns.resolver.query(domain, 'NS')
for i in ns.response.answer:
     for j in i.items:
          print j.to_text()
          
# 查询CNAME记录
cname = dns.resolver.query(domain, 'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()
