#!/usr/bin/bash
dir=$1
brig=${dir}/BRIG_Files
mkdir $brig
mkdir ${brig}/Queries
mkdir ${brig}/Results
for f in ${dir}/GC*/; do
	echo $f
	base=$(basename $f)
	echo $base
	arr=("genomic.fna.gz" "genomic.gbff.gz" "feature_table.txt.gz")
	for a in ${arr[@]}; do
		file=${dir}/${base}/${base}_${a}
		echo $file
		cp $file ${dir}/BRIG_Files/Queries/${base}_${a}
	done
gzip -d ${brig}/Queries/*.gz
done
