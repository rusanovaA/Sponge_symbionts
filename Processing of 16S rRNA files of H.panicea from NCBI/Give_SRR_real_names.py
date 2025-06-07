#!/usr/bin/env python3

import argparse
import os
import csv

parser = argparse.ArgumentParser(description="Select samples by name")
parser.add_argument("-f", "--file", help="File with sample names")
parser.add_argument("-i", "--initial", help="Initial directory")
parser.add_argument("-o", "--output", help="Output dictionary")
args, unknown = parser.parse_known_args()

#Creating dictionary with sample names
names_dict = {}

#Reading the input directory content.
Input_dir_path=args.initial
Input_dir_file_list=os.listdir(Input_dir_path)

#Creating the output directory.
Output_dir_path=args.output
if os.path.exists(Output_dir_path)==False:
    os.mkdir(Output_dir_path)

#Moving files.
with open(args.file,"r") as file:
    for line in csv.reader(file, delimiter='\t'):
        names_dict[line[0]] = line[1]
    
    for SRR, names in names_dict.items():    
        file_SRR_prefix=SRR
        file_name_prefix=names
        r1_file_name=f'{file_SRR_prefix}_1.fastq.gz'
        r2_file_name=f'{file_SRR_prefix}_2.fastq.gz'
        r1_new_file_name=f'{file_name_prefix}_1.fastq.gz'
        r2_new_file_name=f'{file_name_prefix}_2.fastq.gz'
        
        if r1_file_name in Input_dir_file_list:
            os.replace(f'{Input_dir_path}/{r1_file_name}', f'{Output_dir_path}/{r1_new_file_name}')
        else:
            print(f'File {r1_file_name} not found!')
        
        if r2_file_name in Input_dir_file_list:
            os.replace(f'{Input_dir_path}/{r2_file_name}', f'{Output_dir_path}/{r2_new_file_name}')
        else:
            print(f'File {r2_file_name} not found!')