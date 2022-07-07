#!/usr/bin/python3

import os
import sys
import subprocess 

def read_tsv(infile):
    """
    Reads text file with accessions one per line
    """
    ### Read input accessions ###
    with open(infile) as f:
        accessions=[]
        lines = f.readlines()
        for l in lines:
            accession = l.rstrip().split("\t")[0]
            if accession.startswith("GCF") or accession.startswith("GCA"):
                accessions.append(accession)
            else:
                print("WARNING: %s was not formatted correctly, skipping." % l[0] ) 
        f.close()
    return accessions

def download_assembly(accession,outpath):
    """
    Download assemblies from ncbi
    """
    #"wget --recursive -e robots=off --reject "index.html" --no-host-directories --cut-dirs=6" https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/696/305/GCF_001696305.1_UCN72.1/
    #rsync --copy-links --recursive --times --verbose rsync://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/696/305/GCF_001696305.1_UCN72.1 my_dir/
    path_head = "rsync://ftp.ncbi.nlm.nih.gov/genomes/all"
    parts = accession.rpartition("_")
    fullstring = parts[0]
    type_string,identifier = fullstring[:3],fullstring[4:-2]
    path_identifier = "/".join( [identifier[i:i+3] for i in range(0,len(identifier),3) ] )
    path_string = "/".join( [path_head,type_string,path_identifier,accession] )
    cmd = ["rsync", "--copy-links", "--recursive", "--times", "--verbose",path_string,"-P", outpath]
    #cmd = ["wget","--recursive", "-e","robots=off", "--reject", "index.html", "--no-host-directories", "--cut-dirs=6",path_string, "-P", outpath]
    #print(cmd)
    subprocess.run(cmd)

def main():
    ### Set in/out files ###
    infile = sys.argv[1]
    outname = sys.argv[2]
    outdir = os.path.join(os.getcwd(), outname)
    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    accessions = read_tsv(infile)
    for a in accessions:
        download_assembly(a,outdir)

if __name__ == "__main__":
    main()

