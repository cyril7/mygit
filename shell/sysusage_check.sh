#!/bin/bash
WEB_DIR=/tmp/diskmonitor/
# A little CSS and table layout to make the report look a little nicer
echo "<HTML>
<HEAD>
<style>
.titulo{font-size: 1em; color: white; background:#0263CE; padding: 0.1em 0.2em;}
table
{
border-collapse:collapse;
}
table, td, th
{
border:1px solid black;
}
</style>
<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
</HEAD>
<BODY>" > $WEB_DIR/report.html
# View hostname and insert it at the top of the html body
HOST=$(hostname)
echo "Filesystem usage for host <strong>$HOST</strong><br>
Last updated: <strong>$(date "+%Y-%m-%d %H:%M:%S")</strong><br><br>
<table border='10'>
<tr><th class='titulo'>Filesystem</td>
<th class='titulo'>Size</td>
<th class='titulo'>Used</td>
<th class='titulo'>Avail</td>
<th class='titulo'>Use %</td>
<th class='titulo'>Mounted on</td>
</tr>" >> $WEB_DIR/report.html
# Read the output of df -h line by line
while read line; do
echo "<tr><td align='center'>" >> $WEB_DIR/report.html
echo $line | awk '{print $1}' >> $WEB_DIR/report.html
echo "</td><td align='center'>" >> $WEB_DIR/report.html
echo $line | awk '{print $2}' >> $WEB_DIR/report.html
echo "</td><td align='center'>" >> $WEB_DIR/report.html
echo $line | awk '{print $3}' >> $WEB_DIR/report.html
echo "</td><td align='center'>" >> $WEB_DIR/report.html
echo $line | awk '{print $4}' >> $WEB_DIR/report.html

usepercent=$(echo $line | awk '{print $5}' | cut -f 1 -d '%')
if [ "$usepercent" -ge "20" ]; then
    echo "</td><td align='center'><font size="6" color="red">" >> $WEB_DIR/report.html
    echo $line | awk '{print $5}' >> $WEB_DIR/report.html
    echo "</font>" >> $WEB_DIR/report.html
else
    echo "</td><td align='center'><font size="3" color="green">" >> $WEB_DIR/report.html
    echo $line | awk '{print $5}' >> $WEB_DIR/report.html
    echo "</font>" >> $WEB_DIR/report.html
fi


echo "</td><td align='center'>" >> $WEB_DIR/report.html
echo $line | awk '{print $6}' >> $WEB_DIR/report.html
echo "</td></tr>" >> $WEB_DIR/report.html
done < <(df -h | grep -vi filesystem)

echo "</table></BODY></HTML>" >> $WEB_DIR/report.html
