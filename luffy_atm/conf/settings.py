#!/usr/bin/env python
#_*_coding:utf-8_*_

import logging
import os


DASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = "%s/db" % DASE_DIR

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

LOG_PATH = os.path.join(DASE_DIR,"logs")

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s --  %(message)s')

TEANSACTION_TYPE = {
    'repay'     : {'action' : 'plus'  , 'interest' : 0},
    'withadraw' : {'action' : 'minus' , 'interest' : 0.05},
    'transfer'  : {'action' : 'minus' , 'interest' : 0.05},
    'consume'   : {'action' : 'minus' , 'interest' : 0},
}

