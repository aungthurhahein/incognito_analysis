#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
allblocks_file = sys.argv[1]

sc12_block =[]
sc3_block =[]
sc4_block =[]
sc12_desc =[]
sc3_desc =[]
sc4_desc =[]

with open(allblocks_file,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        sc12_block.append(l1_split[0])
        sc12_desc.append(l1_split[1])

        sc3_block.append(l1_split[2])
        sc3_desc.append(l1_split[3])

        sc4_block.append(l1_split[4])
        sc4_desc.append(l1_split[5].strip('\n'))

o1 = open(allblocks_file+"_common", 'w')
o3 = open(allblocks_file+"_common_diffdesc", 'w')
o2 = open(allblocks_file+"_distinct", 'w')
o4= open(allblocks_file+"_common_diffdesc123", 'w')
o5= open(allblocks_file+"_common_diffdesc34", 'w')

del_ind = []
del_ind2 = []
for x, bl1 in enumerate(sc12_block):
    if bl1 in sc3_block and bl1 in sc4_block:
        ind = sc3_block.index(bl1)
        ind2 = sc4_block.index(bl1)
        if (sc12_desc[x].strip() == sc3_desc[ind].strip()) and (sc3_desc[ind].strip() == sc4_desc[ind2].strip()):
            o1.write(bl1+'\t'+sc12_desc[x]+'\t'+sc3_desc[ind]+'\t'+sc4_desc[ind2]+'\n')
            if sc12_desc[x].strip() == sc3_desc[ind].strip():
                o4.write(bl1 + '\t' + sc12_desc[x] + '\t' + sc3_desc[ind] + '\t' + sc4_desc[ind2] + '\n')
            elif sc3_desc[ind].strip() == sc4_desc[ind2].strip():
                o5.write(bl1 + '\t' + sc12_desc[x] + '\t' + sc3_desc[ind] + '\t' + sc4_desc[ind2] + '\n')
            del_ind.append(ind)
            del_ind2.append(ind2)
        else:
            o3.write(bl1 + '\t' + sc12_desc[x] + '\t' + sc3_desc[ind] + '\t' + sc4_desc[ind2] + '\n')
    else:
        o2.write("12"+"\t"+bl1 + '\t' + sc12_desc[x]+'\n')

sc3_new = [i for j, i in enumerate(sc3_block) if j not in del_ind]
sc3_newdesc = [i for j, i in enumerate(sc3_desc) if j not in del_ind]

sc4_new = [i for j, i in enumerate(sc4_block) if j not in del_ind2]
sc4_newdesc = [i for j, i in enumerate(sc4_desc) if j not in del_ind2]

for y, bl3 in enumerate(sc3_new):
    o2.write("3"+"\t"+bl3 + '\t' + sc3_newdesc[y]+'\n')

for z, bl4 in enumerate(sc4_new):
    o2.write("4"+"\t"+bl4 + '\t' + sc4_newdesc[y]+'\n')


# sed -i 's/|E01/-E01/g' *.fasta* && sed -i 's/|E02/-E02/g' *.fasta*

