#Download SRA files parallel
Tool to do parallel fastq dump for multiple SRR entries at once

**Example:** download SRR3034567 up until SRR3034572
`./download_sra_parallel.sh -f 3034567 -l 3034572`

**Installation prequisites:** parallel-fastq-dump should be installed with conda in beforehand
`conda install parallel-fastq-dump`
