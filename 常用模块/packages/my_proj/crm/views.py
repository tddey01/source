#!/usr/bin/env python
#_*_coding:utf-8_*_
"""
import  sys,os
print(dir())
print(__file__)
DASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(DASE_DIR)
sys.path.append(DASE_DIR)
from  proj import settings
"""
'''
# 跨模块导入
import  sys,os
print(dir())
print('file',__file__)
print(os.path.abspath(__file__))
DASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DASE_DIR)
from  proj import settings
'''

"""
# 相对导入模块
from . import models
from ..proj import settings
from  proj import settings
"""

from . import  models
from ..proj import settings
def sayhi():
    print('hello world!')