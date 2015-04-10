#!/usr/bin/python
# -*- coding: utf-8 -*-

import rrdtool
import time,psutil

# 获取网卡入流量
total_input_traffic = psutil.net_io_counters()[1]
# 获取网卡出流量
total_output_traffic = psutil.net_io_counters()[0]
# 获取当前时间戳
starttime=int(time.time())

update=rrdtool.updatev('/tmp/rrdtool/Flow.rrd','%s:%s:%s' % (str(starttime),str(total_input_traffic),str(total_output_traffic)))
print update 

"""
*/5 * * * * /usr/bin/python /tmp/rrdtool/update.py > /dev/null 2>&1
"""
