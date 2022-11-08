#!/usr/bin/env python3

sequences = {}
cont_list = []
good_contigs = []

# read file with contigs
with open("path/to/file.fasta", "r") as file:
        for line in file:
                line=line.rstrip()
                if (line[0] == ">"):
                        header = line
                        sequences[header] = ""
                        #print(line)
                else:
                        data = line
                        sequences[header] += data
                        #print(line)

                
#dictionary_items = sequences.items()
#for item in dictionary_items:
#        print(item)

# read file with the list of required contigs after Whokaryote (DON'T FORGET TO CHANCHED CONTIG TO >CONTIG)
with open("path/to/prokaryote_contig_headers.txt", "r") as cont_list_file:
        for line in cont_list_file:
                line=line.rstrip()
                cont_list.append(line)
                #print(cont_list)

# figure out which contigs are good
for header in sequences.keys():
        if header in cont_list:
                good_contigs.append(header)


# write good contigs
with open("output/prokaryote_contig.fasta", "w+") as good_out:
        for header in good_contigs:
                good_out.write("{}\n{}\n".format(header, sequences[header]))
