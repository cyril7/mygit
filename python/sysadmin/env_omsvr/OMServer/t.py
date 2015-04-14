# -*- coding: utf-8 -*-
import os,sys
from config import *

sysdir=os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.sep.join((sysdir,'modules/'+AUTO_PLATFORM)))

mid="Mid_"+ "1003"
importstring = "from "+mid+" import Modulehandle"

print importstring

exec importstring

help(mid)
