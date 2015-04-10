#!/usr/bin/python
# -*- coding: utf-8 -*-
import difflib
import sys

argv0_list = sys.argv[0].split("\\")
script_name = argv0_list[len(argv0_list) - 1]
try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception, e:
    print "Error; " + str(e)
    print "Usage: " + script_name + " filename1 filename2"
    sys.exit(2)

if textfile1 == "" or textfile2 == "":
    print "Usage: " + script_name + " filename1 filename2"
    sys.exit(2)

def readfile(filename):
    try:
        fileHandle = open(filename, 'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print "Read file Error: " + str(error)
        sys.exit(2)

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)
    
    
