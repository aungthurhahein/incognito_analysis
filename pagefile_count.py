#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
pagelist = sys.argv[1]

page_id = []
page_rule = []
with open(pagelist,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        page_rule.append(l1_split[0])
        page_id.append(l1_split[1].strip('\n'))

uniqpagerule = list(set(page_rule))

for pr in uniqpagerule:
    indexes = [i for i,e in enumerate(page_rule) if e == pr]
    sys.stdout.write(pr+"\t"+str(len(indexes))+'\n')