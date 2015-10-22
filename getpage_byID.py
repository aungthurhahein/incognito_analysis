#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
# still need to fix it to work
# binary data are messing things up

import sys

idlist = sys.argv[1]
pageblocks = sys.argv[2]

rulelist=[">Profile",
            ">youtube",
            ">twitter",
            ">email",
            ">amazon",
            ">ninegag",
            ">incognitomode",
            ">ip",
            ">soundcloud",
            ">http",
            ">webartifact",
            ">password",
            ">webartifact",
            ">url"]

rulehead = []
ruleblock = []
tmp=""
with open(pageblocks,'rb') as f1:
    for x,l1 in enumerate(f1):
        l1_split = l1.split('\t')
        print l1_split
        header = l1_split[0].split('_')[0]
        pageid = l1_split[0].split('-')[1]
        if header in rulelist:
            rulehead.append(pageid.strip('\n'))
            ruleblock.append(l1_split[1])


with open(idlist,'rb') as f2:
    for l2 in f2:
        l2_strip = l2.strip('\n')
        if l2_strip in rulehead:
            ind = rulehead.index(l2_strip)
            sys.stdout.write(rulehead[ind]+'\n')
            sys.stdout.write(ruleblock[ind])

