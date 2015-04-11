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

rrdtool info flow.rrd          : 查看rrd文件的结构信息
rrdtool first flow.rrd         : 查看rrd文件第一个数据的更新时间
rrdtool last flow.rrd          : 查看rrd文件最后一次更新的时间
rrdtool fetch flow.rrd AVERAGE : fetch 根据指定时间,CF查询rrd文件

"""
