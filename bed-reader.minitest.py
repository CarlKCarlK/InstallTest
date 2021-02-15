import numpy as np
from bed_reader import open_bed, sample_file


file_name = sample_file("small.bed")
bed = open_bed(file_name)
print(bed.iid)
#        ['iid1' 'iid2' 'iid3']
print(bed.sid)
#        ['sid1' 'sid2' 'sid3' 'sid4']
print(bed.read())
#       [[ 1.  0. nan  0.]
#        [ 2.  0. nan  2.]
#        [ 0.  1.  2.  0.]]
del bed  # optional: delete bed object


with open_bed(file_name) as bed:
    print(bed.read(np.s_[:, 2]))
#        [[nan]
#         [nan]
#         [ 2.]]

bed = open_bed(file_name, properties={"iid": ["sample1", "sample2", "sample3"]})
print(bed.iid)  # replaced
#  ['sample1' 'sample2' 'sample3']
print(bed.sid)  # same as before
#  ['sid1' 'sid2' 'sid3' 'sid4']
