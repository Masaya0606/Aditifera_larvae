#!/usr/bin/sh
#$ -S /usr/bin/bash
#$ -cwd
#$ -l s_vmem=100G
#$ -l mem_req=100G

mkdir -p coverage
for i in `cat list_Acropora_larvae.txt`
do
singularity exec /usr/local/biotools/s/samtools\:1.9--h46bd0b3_0 samtools depth bam/"$i".bam > coverage/"$i".coverage.txt
done
