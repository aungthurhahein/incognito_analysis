#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

scn1list = sys.argv[1]
scn2list = sys.argv[2]
scn3list = sys.argv[3]
scn4list = sys.argv[4]

scn4_md5 = []
scn4_filepath = []
with open(scn4list,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        scn4_md5.append(l1_split[2])
        scn4_filepath.append(''.join(l1_split[3].strip('\n').split('-')[1:]))

scn3_md5 = []
scn3_filepath = []
with open(scn3list,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        scn3_md5.append(l2_split[2])
        scn3_filepath.append(''.join(l2_split[3].strip('\n').split('-')[1:]))


scn2_md5 = []
scn2_filepath = []
with open(scn2list,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        scn2_md5.append(l3_split[2])
        scn2_filepath.append(''.join(l3_split[3].strip('\n').split('-')[1:]))

scn1_md5 = []
scn1_filepath = []
with open(scn1list,'rb') as f4:
    for l4 in f4:
        l4_split = l4.split('\t')
        scn1_md5.append(l4_split[2])
        scn1_filepath.append(''.join(l4_split[3].strip('\n').split('-')[1:]))

o1= open("43.common",'w')
o2= open("43.diff",'w')
for x,f in enumerate(scn4_filepath):
    md54 = scn4_md5[x]
    if f in scn3_filepath:
        ind = scn3_filepath.index(f)
        md53 = scn3_md5[ind]
        if md54 == md53:
            o1.write(md54+'\t'+f+'\n')
        else:
            o2.write("scn3"+'\t'+md53 + '\t' + f + '\n')
    else:
        o2.write("scn4" + '\t' + md54 + '\t' + f + '\n')


o3= open("32.common",'w')
o4= open("32.diff",'w')
for x,f in enumerate(scn3_filepath):
    md53 = scn3_md5[x]
    if f in scn2_filepath:
        ind = scn2_filepath.index(f)
        md52 = scn2_md5[ind]
        if md53 == md52:
            o3.write(md53+'\t'+f+'\n')
        else:
            o4.write("scn2"+"\t"+md52 + '\t' + f + '\n')
    else:
        o4.write("scn3" + "\t"+md53 + '\t' + f + '\n')

o5 = open("21.common", 'w')
o6 = open("21.diff", 'w')
for x,f in enumerate(scn2_filepath):
    md52 = scn2_md5[x]
    if f in scn1_filepath:
        ind = scn1_filepath.index(f)
        md51 = scn1_md5[ind]
        if md52 == md51:
            o5.write(md52 + '\t' + f + '\n')
        else:
            o6.write("scn1" +"\t"+ md51 + '\t' + f + '\n')
    else:
        o6.write("scn2" + "\t"+md52 + '\t' + f + '\n')



