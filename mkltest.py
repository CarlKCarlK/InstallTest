from pysnptools.snpreader import Bed
from fastlmm.util import compute_auto_pcs
from fastlmm.association import single_snp_select
from fastlmm.util import example_file # Download and return local file name

# define file names
bed_fn = example_file('tests/datasets/synth/all.*','*.bed')
snp_reader = Bed(bed_fn, count_A1=True)
pheno_fn = example_file("tests/datasets/synth/pheno_10_causals.txt")
cov_fn = example_file("tests/datasets/synth/cov.txt")

# find number of PCs
pcs = compute_auto_pcs(bed_fn,count_A1=True)
print("selected number of PCs:", pcs["vals"].shape[1])

# test on chr5
test_snps = snp_reader[:,snp_reader.pos[:,0] == 5]

results_df = single_snp_select(test_snps=test_snps, G=snp_reader, pheno=pheno_fn, covar=pcs, GB_goal=2)
results_df.head()