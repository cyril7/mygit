#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()

chart = workbook.add_chart({'type': 'column'})

title = [u'业务名称',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日',u'平均流量']
buname= [u'业务官网',u'新闻中心',u'购物频道',u'体育频道',u'亲子频道']

data = [
    [150,152,158,149,155,145,148],
    [89,88,95,93,98,100,99],
    [201,200,198,175,170,198,195],
    [75,77,78,78,74,70,79],
    [88,85,87,90,93,88,84],
]
format=workbook.add_format()

# 定义format对象单元格边框加粗(1像素)的格式
format.set_border(1)

# 定义format_title格式对象
format_title=workbook.add_format()
# 单元格边框加粗
format_title.set_border(1)
# 单元格背景颜色
format_title.set_bg_color('#cccccc')
# 单元格居中对齐
format_title.set_align('center')
# 单元格居中对齐
format_title.set_bold()

# 计算平均数时的格式
format_ave=workbook.add_format()
format_ave.set_border(1)
format_ave.set_num_format('0.00')

worksheet.write_row('A1',title,format_title)
worksheet.write_column('A2', buname,format)
worksheet.write_row('B2', data[0],format)
worksheet.write_row('B3', data[1],format)
worksheet.write_row('B4', data[2],format)
worksheet.write_row('B5', data[3],format)
worksheet.write_row('B6', data[4],format)

# 定义图表数据系列函数
def chart_series(cur_row):
    # 计算(AVERAGE函数)频道周平均流量
    worksheet.write_formula('I'+cur_row, \
     '=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)

    chart.add_series({
        'categories': '=Sheet1!$B$1:$H$1', # "星期一至星期日"作为X轴
        'values':     '=Sheet1!$B$'+cur_row+':$H$'+cur_row, # 频道一周所有数据作为数据区域
        'line':       {'color': 'black'}, # 线条颜色为black
        'name':	'=Sheet1!$A$'+cur_row, # 引用业务名称为图例项
    })

for row in range(2, 7): # 数据域以第1至6行进行图表系列函数调用
    chart_series(str(row))

# 设置X轴表格格式,本示例不启用
#chart.set_table()
# 设置图表样式,本示例不启用
#chart.set_style(30)

# 图表大小
chart.set_size({'width': 577, 'height': 287})
# 图表上方大标题
chart.set_title ({'name': u'业务流量周报图表'})
# 图表左侧(y轴)小标题
chart.set_y_axis({'name': 'Mb/s'})

# 在A8单元格插入图表
worksheet.insert_chart('A8', chart)
workbook.close()
