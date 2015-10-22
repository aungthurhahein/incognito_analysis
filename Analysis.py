#! /usr/bin/env/ python

"""
# 
# usage: yara pattern scanning targed file with defined rules
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import yara

rule_file = sys.argv[1]
scanned_file = sys.argv[2]

def printout(data):
    print data
    yara.CALLBACK_CONTINUE

rules = yara.compile(filepath=rule_file)
matches = rules.match(scanned_file, callback= printout)
