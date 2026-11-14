import fastlmm  # noqa
from fastlmm.association import single_snp, single_snp_scale  # noqa
from fastlmm.util import example_file

# The single_snp docstring example: a genome-wide association on sample data.
pheno_fn = example_file("fastlmm/feature_selection/examples/toydata.phe")
test_snps = example_file("fastlmm/feature_selection/examples/toydata.5chrom.*", "*.bed")
results_dataframe = single_snp(test_snps=test_snps, pheno=pheno_fn, count_A1=False)
top = results_dataframe.iloc[0]
print(top.SNP, round(top.PValue, 7), len(results_dataframe))
assert top.SNP == "null_576"
assert round(top.PValue, 7) == 1e-07
assert len(results_dataframe) == 10_000

print("OK")
