#!/usr/bin/env python3

from matplotlib import pyplot as plt
import sys
import argparse

parser = argparse.ArgumentParser(description="Check distribution of MAPQ in SAM file")
parser.add_argument("-f", "--file", help="SAM file")
parser.add_argument("-o", "--output", help="Output to histogram")
args, unknown = parser.parse_known_args()

# read sam file
mapq_list = []
with open(args.file, "r") as file:
        for line in file:
                if (line[0] == "@"):
                        continue                
                line=line.rstrip().split('\t')
                if (line[2] == "*") or (line[9] == "*"):
                        continue
                mapq_list.append(int(line[4]))
                #print(line[4])
#print(mapq_list)

plt.hist(mapq_list, alpha=0.5)
plt.title('Distribution of MAPQ score')
plt.xlabel('MAPQ')
plt.ylabel('count')
plt.savefig(args.output)