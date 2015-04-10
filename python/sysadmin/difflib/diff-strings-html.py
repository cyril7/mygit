#!/usr/bin/python
# -*- coding: utf-8 -*-
import difflib

# 多行字符串
text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""
# 使用换行符分割
text1_lines = text1.splitlines()

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

# 生成HTML格式
d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)
