#!/bin/bash



pheno_1=$1
pheno_2=$2
outname=$3


ldsc.py --rg $pheno_1,$pheno_2 --ref-ld-chr refs/eur_w_ld_chr/ --w-ld-chr refs/eur_w_ld_chr/ --rgdf --out $outname




