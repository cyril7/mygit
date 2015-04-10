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
 "CDEF:total=inoctets,outoctets,+",
 "LINE1:total#FF8833:Total traffic",
 "AREA:inoctets#00FF00:In traffic",
 "LINE1:outoctets#0000FF:Out traffic",
 "HRULE:6144#FF0000:Alarm value\\r",
 "CDEF:inbits=inoctets,8,*",
 "CDEF:outbits=outoctets,8,*",
 "COMMENT:\\r",
 "COMMENT:\\r",
 "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
 "COMMENT:   ",
 "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps",
 "COMMENT:  ",
 "GPRINT:inbits:MIN:MIN In traffic\: %6.2lf %Sbps\\r",
 "COMMENT: ",
 "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
 "COMMENT: ",
 "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps",
 "COMMENT: ",
 "GPRINT:outbits:MIN:MIN Out traffic\: %6.2lf %Sbps\\r")
