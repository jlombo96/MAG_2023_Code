#!/usr/bin/python3
#fix_coordinates.py annotations.tsv contigs.tsv 

import pandas as pd
import sys

annotations, contigs = pd.read_csv( sys.argv[1], sep="\t", names=["contig","start","end","desc","symbol"] ), pd.read_csv( sys.argv[2], names=["contig","astart","aend"], sep="\t")
df = annotations.merge(contigs,on="contig",how="left")
df["nstart"] = df["astart"] + df["start"]
df["nend"] = df["astart"] + df["end"]
print(df)
columns_to_keep = ["nstart","nend","desc","symbol"]
df = df[columns_to_keep]
print(df)
df.to_csv(sys.argv[1].replace(".tsv", ".fixed.tsv"),sep="\t", index=False)