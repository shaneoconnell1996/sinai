#!/usr/env/python2.7
import itertools
import numpy as np
import subprocess
import glob
import time
print 'processing....'

files = glob.glob('/data2/soconnell/gwas/mssm/sumstats/munged_stats/*')

print 'read files... beginning loop'

pairs = itertools.combinations(files,2)



for rgpair in pairs:
	jobs = subprocess.check_output('squeue -u soconnell | wc -l',shell=True)
	while int(jobs) > 70:
		print 'sleeping while we wait to not clog the cluster :) '
		time.sleep(60)
		jobs = subprocess.check_output('squeue -u soconnell | wc -l',shell=True)
	else:
		pheno_1=rgpair[0]
		pheno_2=rgpair[1]
		outname='{}_rg_{}'.format(pheno_1.split('/')[-1].split('.')[0],pheno_2.split('/')[-1].split('.')[0])
	

		subprocess.call(['sbatch', '-n', '1', '-J', 'rg','gen_corr.sh','{}'.format(pheno_1),'{}'.format(pheno_2),'{}'.format(outname)])
	
	
	
