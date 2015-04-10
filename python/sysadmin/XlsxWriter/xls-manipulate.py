#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
# 设定第一列(A)宽度为20像素
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
#bold = workbook.add_format({'bold': True})
# 设置为粗体
bold = workbook.add_format()
bold.set_bold()

# Write some simple text.
# A1单元格写入 hello
worksheet.write('A1', 'Hello')

# Text with formatting.
# A2 单元格写入粗体
worksheet.write('A2', 'World', bold)

# 写入中文
worksheet.write('B2', u'中文测试', bold)

# Write some numbers, with row/column notation.
# 用行列表示法写入32和35.5
# 行列表示法的单元格下标以0作为起始值,'3,0'等价于'A5'
worksheet.write(2, 0, 32)
worksheet.write(3, 0, 35.5)

# 求A3,A4的和,并结果写入A4
worksheet.write(4, 0, '=SUM(A3:A4)')

# Insert an image.
# 插入图片
worksheet.insert_image('B5', 'img/python-logo.png')

workbook.close()
