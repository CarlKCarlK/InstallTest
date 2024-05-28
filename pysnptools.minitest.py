# Download a sample file
from pysnptools.util import example_file
import sys
import platform

bed_file = example_file("pysnptools/examples/toydata.5chrom.*", "*.bed")
from pysnptools.snpreader import Bed

bed = Bed(bed_file, count_A1=False)
val0 = bed[:, 0].read().val  # Read 1st SNP
print(val0.shape)  # Shape of the NumPy array
assert val0.shape == (500, 1)

val_all = bed.read().val  # Read all variants
print(val_all.shape)  # Shape of the NumPy array
assert val_all.shape == (500, 10_000)

# cmk
# try:
#     from pysnptools.distreader import Bgen

#     BGEN_READER_AVAILABLE = True
# except ImportError:
#     BGEN_READER_AVAILABLE = False
#     print("Bgen reader is not available on this platform")

# if BGEN_READER_AVAILABLE:
#     bgen_file = example_file("pysnptools/examples/example.bgen")

#     # Read from the file
#     bgen = Bgen(bgen_file)  # Create a reader
#     probs0 = bgen[:, 0].read().val  # Read 1st SNP
#     print(probs0.shape)  # Shape of the NumPy array
#     assert probs0.shape == (500, 1, 3)

#     probs_all = bgen.read().val  # Read all variants
#     print(probs_all.shape)  # Shape of the NumPy array
#     assert probs_all.shape == (500, 199, 3)
