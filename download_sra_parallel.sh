#!/bin/bash

## This script uses parallel-fastq-dump (conda install parallel-fastq-dump) to download for multiple SRR entries at once
## nohup ./download_sra_parallel.sh -f 3034567 -l 3034572 -c 20 > nohup.txt &

#Read input parameters
FIRST=
LAST=
while [ "$1" != "" ]; do
    case $1 in
        -f )        shift
                    FIRST=$1
                    ;;
        -l )        shift
                    LAST=$1
                    ;;
        -c )	    shift
                CORES=$1
                ;;
    esac
    shift
done

echo
echo
echo "PARALLEL FASTQ DUMP"
echo
echo "Getting fastq files for SRR$FIRST up to SRR$LAST"
echo

mkdir tmp
if [ $FIRST -eq $LAST ]; then
    parallel-fastq-dump -s SRR$FIRST -t $CORES -O . --tmpdir tmp
else
    for i in $(seq $FIRST 1 $LAST)
    do
	echo "Downloading SRR$i"
	parallel-fastq-dump -s SRR$i -t $CORES -O . --tmpdir tmp
    rm -rf ~/ncbi/public/sra/SRR$i.sra.cache
    done
fi
rm -rf tmp
