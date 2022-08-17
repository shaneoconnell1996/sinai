#!/bin/bash

source /data/soconnell/phd/test_scripts/set_up_env.sh ldsc


file=$1
N_par=$2
out=$3


munge_sumstats.py --sumstats $file --out $out --p "pval(-log10)" --N $N_par --chunksize 500000 --log10pvals --merge-alleles /data2/soconnell/gwas/mssm/sumstats/refs/w_hm3.snplist


