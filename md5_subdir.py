#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import os
import sys
from subprocess import call

rootdir = str(sys.argv[1])
o = open(rootdir+".md5",'w')

for subdir, dirs, files in os.walk(rootdir):
    for f in files:
        # print os.path.join(subdir, f)
        fpath = os.path.join(subdir, f)
        call("md5sum " + fpath, shell=True)
