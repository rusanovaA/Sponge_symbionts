# Sponge_symbionts

## Workflow for identification and characterisation of sponge-specific bacterial symbionts

### Introduction
Sponges (phylum *Porifera*) form symbiotic relationship with the community of microorganisms. Sponges and their symbionts produce various pharmacologically active substances. These communities differ in taxonomic composition from those of the surrounding seawater. Metagenomic analysis of the microbiome allows to find out the taxonomic diversity and properties of the microbial community[^1, 2].
### Aim, tasks and data
The aim of the project is to prove the presence and investigate the properties of bacterial symbionts of sponges.

Tasks:
+ Assembled MAGs of potentil symbionts
+ Pick up probes to the 16s rRNA of each potential symbiont for conducting FISH (fluorescent in situ hybridization)
+ Find out what features already studied sponge symbionts have and look for them from our guys

For this workflow you need prior analysed data of 16S rRNA from microbial communities of sponges and assembled contigs from shotgun metagenomic reads from the same communities.

### System requirements and programs used
* Ubuntu 20.04
#### Binning
* Bowtie2 v2.3.2 (http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml)
* MetaBAT2 v1.7 (https://bitbucket.org/berkeleylab/metabat/src/master/)
* MaxBin2 v2.2.4 (https://sourceforge.net/projects/maxbin2/)
* CONCOCT v1.1 (https://github.com/BinPro/CONCOCT)
* DAS Tool v1.1.2 (https://github.com/cmks/DAS_Tool)
* CheckM v1.0.18 (https://github.com/Ecogenomics/CheckM/wiki)
#### Annotation
* MetaGeneMark (http://exon.gatech.edu/meta_gmhmmp.cgi)
* GTDB-Tk based on the Genome Taxonomy Database (GTDB) v1.1.0 (https://github.com/Ecogenomics/GTDBTk)
* RAST (https://rast.nmpdr.org/)
* DIAMOND with NCBI nr databes (https://github.com/bbuchfink/diamond)
* CRISPRCasTyper (https://crisprcastyper.crispr.dk/#/submit)
* CRISPRCasFinder (https://crisprcas.i2bc.paris-saclay.fr/CrisprCasFinder/Index)
* AcRanker (https://github.com/amina01/AcRanker)
* antiSMASH bacterial version (https://antismash.secondarymetabolites.org/#!/start)
* BlastKOALA (https://www.kegg.jp/blastkoala/)
* KofamKOALA (https://www.genome.jp/tools/kofamkoala/)
* KEGG Mapper (https://www.kegg.jp/kegg/mapper/reconstruct.html)
* TASmania (https://shiny.bioinformatics.unibe.ch/apps/tasmania/)
* DefenseFinder (https://defense-finder.mdmparis-lab.com/)
* PADLOC (https://padloc.otago.ac.nz/padloc/)
* PHASTER (https://phaster.ca/)
* Barrnap (https://github.com/tseemann/barrnap)
* WebMGA (http://weizhong-lab.ucsd.edu/webMGA/server/)
#### FISH probes desing
* DECIPHER Design Probes (http://www2.decipher.codes/DesignProbes.html#:~:text=DECIPHER%20%2D%20Design%20FISH%20Probes&text=Use%20DECIPHER's%20Design%20Probes%20web,try%20our%2016S%20Oligos%20tool.)
* mathFISH (http://mathfish.cee.wisc.edu/probeaff.html)

### Workflow
#### Binning of MAGs (metagenome assembled genomes) and it's identification
We found out that each of our investigated sponge species was dominated by several sponge specific OTUs of V3-V4 region of bacteria 16S rRNA gene. So, we decided to binned metagenomic contigs and find those MAGs in which there were dominant 16S.
> You can find all the programs from the "Binning" section on the KBase server (https://www.kbase.us/) and run them online
For contig binning we used MaxBin2, MetaBat2 and CONCOCT and varied the parameter of the minimum contig length (1000, 2500 bp). CheckM was used for assessing the quality of binns.
Metagenomic contigs from each sample were blasted with OTU sequences. 

```
makeblastdb -in contigs.fasta -dbtype nucl
blastn -db contigs.fasta -query OTU_table.fasta -outfmt "6 qseqid sseqid stitle pident length mismatch gapopen qstart qend sstart send evalue bitscore" -out blast_16S

```
Contigs with the desired sequences were searched in results from the three binning tools. The bin that contained the OTU of the dominant bacteria was considered as MAG of this potential bacterial symbiont. If there were several bins, DAS Tool was used. 

#### Annotation of metagenome assemblies and MAGs
We have tried a large number of different programs to annotate the results.

##### Predictins of proteins function with different databases
MetaGeneMark were used to gene prediction in metagenomes and MAGs (output as gff file, protein and nucleotide sequences).
Protein sequences and contigs were annotetad with:
* RAST - the NMPDR, SEED-based, prokaryotic genome annotation service
* DIAMOND with NCBI nr databes

```
diamond makedb --in ./nr.fasta -d nr
diamond blastx -d  ./nr -q ./myfile.faa -o ./name_out --more-sensitive -k 20 -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore

```
* BlastKOALA - KEGG's internal annotation tool for K number assignment of KEGG GENES using SSEARCH computation
* KofamKOALA - assigns K numbers to the user's sequence data by HMMER/HMMSEARCH against KOfam (a customized HMM database of KEGG Orthologs (KOs))
* KEGG Mapper - "reconstructs" KEGG pathway maps and other network entities from a set of K numbers (KO identifiers)
* WebMGA (Server) - function annotation with different databases, such as cog, kog, prk, pfam, tigrfam

##### Specialized programs
These tools were used to search for specific features of communities and MAGs:
###### Bacterial and phages defense systems
* CRISPRCasTyper - CRISPR-Cas prediction and classification tool
* CRISPRCasFinder program enables the easy detection of CRISPRs and cas genes in user-submitted sequence dat
* AcRanker - a machine learning system developed in python that ranks proteins in a proteome as per their Anti-CRISPR tendencies predicted using sequence features
* DefenseFinder - analyses of antiviral system
* PADLOC - and another one with a set of slightly different systems
* TASmania - annotation of toxins ans=d antitoxins
###### Another programs
* GTDB-Tk - toolkit for assigning objective taxonomic classifications to bacterial and archaeal genomes based on the Genome Database Taxonomy (GTDB)
* antiSMASH - allows the rapid genome-wide identification, annotation and analysis of secondary metabolite biosynthesis gene clusters in bacterial and fungal genomes
* Barrnap - predicts the location of ribosomal RNA genes
* PHASTER - identification and annotation of prophage sequences

### Results
+ We got high and medium quality MAGs for each of our sponges potential symbionts
![image](https://user-images.githubusercontent.com/90505680/171190421-e53ad8bf-5fe2-4912-bd53-3a25834a2664.png)
+ The FISH probes were designed with DECIPHER's Design Probes web tool and checked with mathFISH with different parameters of the experiment. They will be tested in vivo soon
+ Symbiont features: eukaryotic-like protein domains (ELPs), bacteria defence systemsproduction of secondary metabolites as chemical defensive molecules,  production of vitamins[^3]. One of our studied symbionts had a сobalamin biosynthesis pathway and different defense systems (RM type II and Hachiman & RM type I).
![image](https://user-images.githubusercontent.com/90505680/171189750-1513aec4-d566-4f6b-a351-e5627a87e3df.png)
![image](https://user-images.githubusercontent.com/90505680/171189767-11ff0875-9d3e-4de9-bb51-b30fa58ddeb3.png)

### Conclusions
We investigated different metods of binning and annotation of contigs and MAGs. The use of a large number of different programs allows you to get more complete information about the object of research, while the use of programs aimed at the study of the same target can help supplement the information when combining the results. For example, the programs for annotation of bacterial defense systems PADLOC and DefenseFinder differ slightly in the set of systems, so they can be used in addition to each other. Toolkits for full annotation of all proteins can also rely on different databases. Therefore, it is good to have a large set of tools for data analysis in stock.

### References
1. Knobloch S, Jóhannsson R, Marteinsson V Bacterial diversity in the marine sponge Halichondria panicea from Icelandic waters and host specificity of its dominant symbiont Candidatus Halichondribacter symbioticus FEMS Microbiol Ecol 2019 Jan 1;95
2. Gauthier M EA, Watson JR and Degnan SM 2016 Draft Genomes Shed Light on the Dual Bacterial Symbiosis that Dominates the Microbiome of the Coral Reef Sponge Amphimedon queenslandica Front Mar Sci 3:196
3. Thomas, T Rusch D DeMaere M et al Functional genomic signatures of sponge bacteria reveal unique and shared features of symbiosis ISME J 4 1557-1567 (2010)
