# -*- coding: utf-8 -*-
DBNAME = 'WebMonitor'
DBUSER = 'root'
DBPASSWORD = ''
DBHOST = '127.0.0.1'


# 修改成探测运营商网络代码(重要)
# settings.py 中定义IDC={'ct':'电信', 'cnc':'网通', 'cmcc':'移动'}
IDC = 'ct'

# 连接的等待时间
CONNECTTIMEOUT = 5
# 请求超时时间
TIMEOUT = 10

# 告警邮件地址
MAILTO = 'user1@domain.com,user2@domain.com'

# 告警手机号码
MOBILETO = '13333334444'
