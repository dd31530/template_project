#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
+----------------------------------------------------------------------------+
| messagesUtils:  toolbox for displaying formated messages                   |
+---------+----------+----------+--------------------------------------------+
| version | datecode | author   | history                                    |
+---------+----------+----------+--------------------------------------------+
| 1.0     | 151214   | DD       | creation                                   |
+---------+----------+----------+--------------------------------------------+
'''

VERSION = 'v1.0_151214'

##############################################################################
# external modules
##############################################################################


import sys
import inspect
import ast
import datetime


##############################################################################
# local modules
##############################################################################




##############################################################################
# functions 
##############################################################################


def header():
   '''
   displays current module docstring
   '''
   f=inspect.stack()[1][1]
   m=ast.parse(''.join(open(f)))
   print "\n%s" % ast.get_docstring(m)


def banner(mess):
   '''
   displays banner message
   '''
   sep = '\n+'+76*'-'+'+\n'
   mess = '| ' +mess + (75-len(mess))*' ' + '|'
   print sep, mess, sep


def footer(code=0):
   '''
   displays current module execution ending
   '''
   banner('end of ' + sys.argv[0])
   sys.exit(code)


##############################################################################
# main
##############################################################################


if  __name__ == '__main__':
   from logUtils import Logger
   header()
   Logger.logr.info("Autotest: header() ( ^^^^ above ^^^^ )")
   banner("Autotest: banner()") 
   Logger.logr.info("Autotest: footer() ( vvvv below vvvv )")
   footer()


##############################################################################
# eof
##############################################################################
