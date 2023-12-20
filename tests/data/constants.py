import numpy as np
import pandas as pd


l1 = [1,2,3]

s1 = pd.Series([1,2,3], index=list('abc'))
s2 = pd.Series([1,5,3,10], index=list('bcad'))


df1 = pd.DataFrame(np.eye(3))
df2 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'), columns=list('ABCD'))

df3 = pd.DataFrame({
    'chr': ['chr1', 'chr7', 'chr10', 'chr21', 'chrX', 'chrY', ],
    'locus': [443, 6, 314, 800, 454523, 10,],
})

df4 = pd.DataFrame({
    'gene1': {'sample1':23, 'sample2':10, 'sample3':0},
    'gene2': {'sample1':10, 'sample2':40, 'sample3':120},
    'gene3': {'sample1':0, 'sample2':10, 'sample3':78},
})

annot = {
    'gene1': {
        'geneID': '03455',
        'geneName': 'SAT',
        'start': 4,
        'end': 100,
    },
    'gene2': {
        'geneID': '0455',
        'geneName': 'BAT4',
        'start': 40,
        'end': 1600,
    },
}

samples = {
    'sample1': {
        'sample_name': 'sample1',
        'age' :45,
        'gender': 'F',
    },
    'sample2': {
        'sample_name': 'sample2',
        'age' :58,
        'gender': 'M',
    },
}

