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

# FaST-LMM 1.1: float32 on the CPU (CI runners have no GPU) finds the same top SNP,
# and every p-value is within float32's expected difference from float64.
import numpy as np  # noqa: E402

results_float32 = single_snp(test_snps=test_snps, pheno=pheno_fn, count_A1=False, dtype="float32")
assert results_float32.iloc[0].SNP == "null_576"
both = results_dataframe.set_index("SNP").PValue.to_frame("float64").join(
    results_float32.set_index("SNP").PValue.rename("float32"))
largest = float(np.max(np.abs(np.log10(both["float32"]) - np.log10(both["float64"]))))
print("float32 max |delta log10 p|:", largest)
# Observed 5.3e-6 on Linux with OpenBLAS; 1e-3 leaves room for other platforms' BLAS
# while still catching a broken float32 path.
assert largest < 1e-3

print("OK")
