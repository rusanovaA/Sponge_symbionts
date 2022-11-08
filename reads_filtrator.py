from Bio import SeqIO
import sys
import argparse

parser = argparse.ArgumentParser(description="Filter corrupted aligned reads from initial file")
parser.add_argument("-f", "--file", help="Aligned reads fastq")
parser.add_argument("-i", "--initial", help="Initial fastq file")
parser.add_argument("-o", "--output", help="Output fastq file")
#args = parser.parse_args()
args, unknown = parser.parse_known_args()

aligned_names = set()
for read in SeqIO.parse(args.file, "fastq"):
    aligned_names.add(read.id)
#print(aligned_names)

with open(args.output, "w") as output:
    for record in SeqIO.parse(args.initial, "fastq"):
        if record.id in aligned_names:
            SeqIO.write(record, output, "fastq")
        else:
            continue
    