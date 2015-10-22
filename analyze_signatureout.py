#! /usr/bin/env/ python

"""
# To reformat signature analysis output
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

sig_file = sys.argv[1]
count = 0
result_format = {}
result_offset = {}
result_binary = {}

f2 = open(sig_file+"_text", 'w')
f3 = open(sig_file+"_offset", 'w')
f4 = open(sig_file+"_binary", 'w')

with open(sig_file,'rb') as f1:
    for line in f1:
        line_split = line.split()
        if 'Rule:' in line:
            tmprule_cat = ""
            count += 1
            rule_split = line.split(':')
            rulecat = rule_split[1].strip()
            tmprule_cat = rulecat+"_" + str(count)
        elif "Owner:" in line:
            pid = line.split(":")[1].strip('\n')
        elif len(line_split) > 5:
            if tmprule_cat not in result_format:
                result_format[tmprule_cat] = pid+"\t"+line_split[17]  # text
                result_offset[tmprule_cat] = line_split[0]+","  # offset
                result_binary[tmprule_cat] = str(line_split[1:16])+ ","  # binary
            else:
                result_format[tmprule_cat] += line_split[17]
                result_offset[tmprule_cat] += line_split[0] + ","
                result_binary[tmprule_cat] += str(line_split[1:16])+ ","


keylist = result_format.keys()
keylist.sort()
for key in keylist:
    sys.stdout.write(key+'\t'+result_format[key]+"\n")
    f2.write(key+'\t'+result_format[key]+"\n")
for key in keylist:
    sys.stdout.write(key+'\t'+result_offset[key]+"\n")
    f3.write(key+'\t'+result_offset[key]+"\n")
for key in keylist:
    sys.stdout.write(key+'\t'+result_binary[key]+"\n")
    f4.write(key+'\t'+result_binary[key]+"\n")







