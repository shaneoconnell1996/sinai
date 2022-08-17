#!/usr/env/python2.7

import pandas as pd
import numpy as np
import subprocess
print 'processing....'

master_df = pd.read_csv('/data2/soconnell/gwas/mssm/sumstats/master_file.csv',sep='\t')

print 'read master file... beginning loop'

for i in master_df[['files','N(fullscan)','recoded_pheno_codes']].values:
	sumstat=i[0]
	N=int(i[1])
	out_pheno=i[2]
	

	subprocess.call(['sbatch', '-n', '1', '-J', 'munge','small_munge_script.sh','{}'.format(sumstat),'{}'.format(N),'{}'.format(out_pheno)])
	
