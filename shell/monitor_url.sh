#!/bin/bash

# https://webutility.io/csv-to-chart-online
# https://csv2chart.com/
# This creates a CSV file that can be uploaded to Google Docs where you can insert a chart to graph the values

LOG_FILE='/root/ytmon_tools/url_monitor.log'
#URL="www.google.com"
URL="https://www.zhihu.com"

if [ ! -f $LOG_FILE ]; then # add CSV column headers
  echo Date,Total Time,Redirect Time,DNS Lookup,Connect,App Connect,Pretransfer,starttransfer,Status Code > $LOG_FILE
fi

#/usr/bin/curl -m 9 -L -w "$(date),%{time_total},%{time_redirect},%{time_namelookup},%{time_connect},%{time_appconnect},%{time_pretransfer},%{time_starttransfer},%{http_code}\n" -o /dev/null -s "https://example.com/monitor" >> $LOG_FILE
#/usr/bin/curl -m 9 -L -w "$(date "+%Y%m%d_%H:%M:%S"),%{time_total},%{time_redirect},%{time_namelookup},%{time_connect},%{time_appconnect},%{time_pretransfer},%{time_starttransfer},%{http_code}\n" -o /dev/null -s "${URL}" >> $LOG_FILE
/usr/bin/curl -m 9 -L -w "$(date "+%m%d_%H:%M:%S"),%{time_total},%{time_redirect},%{time_namelookup},%{time_connect},%{time_appconnect},%{time_pretransfer},%{time_starttransfer},%{http_code}\n" -o /dev/null -s "${URL}" >> $LOG_FILE
