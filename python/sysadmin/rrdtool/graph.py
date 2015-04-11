#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
该DEMO的关键参数是使用了--x-grid定义X轴网格刻度
DEF指定数据源
使用CDEF合并数据
HRULE绘制水平线(告警线)
GPRINT输出最大值,最小值,平均值等
"""

import rrdtool
import time

# 定义图表上方大标题
title="Server network  traffic flow ("+time.strftime('%Y-%m-%d',time.localtime(time.time()))+")"

"""
"--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H"
MINUTE:12 --> 表示控制每隔12分钟放置一根次要格线
HOUR:1    --> 表示控制每隔1个小时放置一根主要格线
HOUR:1    --> 表示控制1个小时输出一个label标签
0:%H      --> 

"""

rrdtool.graph( "Flow.png", "--start", "-1d","--vertical-label=Bytes/s","--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H",\
 "--width","650","--height","230","--title",title,
 "DEF:inoctets=Flow.rrd:eth0_in:AVERAGE", # 指定网卡入流量数据源DS及CF
 "DEF:outoctets=Flow.rrd:eth0_out:AVERAGE", # 指定网卡出流量数据DS及CF
 "CDEF:total=inoctets,outoctets,+",        # 通过CDEF合并网卡出入流量,得出总流量total
 "LINE1:total#FF8833:Total traffic",   # 以线条方式绘制总流量
 "AREA:inoctets#00FF00:In traffic",    # 以面积方式绘制入流量
 "LINE1:outoctets#0000FF:Out traffic", # 以线条方式绘制出流量
 "HRULE:6144#FF0000:Alarm value\\r",  # 绘制水平线,作为告警线,阈值为6.1K
 "CDEF:inbits=inoctets,8,*",         # 将入流量换算成bit,即*8,计算结果给inbits
 "CDEF:outbits=outoctets,8,*",       # 将出流量换算成bit,即*8,计算结果给inbits
 "COMMENT:\\r",                      # 在网格下方输出个换行符
 "COMMENT:\\r",
 "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps", # 绘制入流量平均值
 "COMMENT:   ",
 "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps",   # 绘制入流量最大值
 "COMMENT:  ",
 "GPRINT:inbits:MIN:MIN In traffic\: %6.2lf %Sbps\\r", # 绘制入流量最小值
 "COMMENT: ",
 "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps", # 绘制出流量平均值
 "COMMENT: ",
 "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps", # 绘制出流量最大值
 "COMMENT: ",
 "GPRINT:outbits:MIN:MIN Out traffic\: %6.2lf %Sbps\\r") # 绘制出流量最小值
