from unittest import TestCase
from ddt import ddt, data, unpack

from src.rnaseqdata import AnnotData
from tests.data.constants import *

@ddt
class TestAnnotData(TestCase):

    @data(
        [None, None, 0, {}],
        [1, None, 1, {}],
        [None, {'a':{}}, 0, {'a':{}}],
    )
    @unpack
    def test_init(self, axis, data, expect_axis, expect_data):
        c = AnnotData(axis, data)
        assert c.axis == expect_axis
        assert c.data.to_dict() == expect_data
    
    @data(
        [None, None, (2,3)],
        [None, ['sample_name', 'age', 'gender'], (2,3)],
        [['sample1', 'sample2'], ['sample_name', 'age', 'gender'], (2,3)],
        [['sample1', 'sample3'], ['sample_name', 'age', 'gender'], (2,3)],
        [['sample1',], ['sample_name', 'age',], (1,2)],
        [['sample1',], ['sample_name', 'age', 'level'], (1,3)],
    )
    @unpack
    def test_to_df_1(self, key1, key2, expect_shape):
        c = AnnotData(0, samples)
        res = c.to_df(key1, key2)
        assert res.shape == expect_shape

    @data(
        [None, None, (4,2)],
        [None, ['geneID', 'geneName', 'start', 'end'], (4,2)],
        [['gene1', 'gene2'], None, (4,2)],
        [['gene1', 'gene2'], ['geneID', 'geneName', 'start', 'end'], (4,2)],
        [['gene1',], ['start', 'geneName', 'end'], (3,1)],
        [['gene2', 'gene1'], None, (4,2)],
        # missing key1 or key2
        [['gene1', 'gene3'], None, (4,2)],
        [None, ['geneID', 'geneName', 'GO'], (3,2)],
    )
    @unpack
    def test_to_df_2(self, key1, key2, expect_shape):
        c = AnnotData(1, annot)
        res = c.to_df(key1, key2)
        assert res.shape == expect_shape

    @data(
        [0, None, None, (0,0)],
        [0, ['sample1', 'sample2'], None, (2,0)],
        [0, ['sample1', 'sampleX'], None, (2,0)],
        [1, None, None, (0,0)],
        [1, ['gene1', 'gene2'], None, (0,2)],
        [1, ['gene1', 'geneX'], None, (0,2)],
    )
    @unpack
    def test_to_df_empty(self, axis, key1, key2, expect_shape):
        c = AnnotData(axis)
        res = c.to_df(key1, key2)
        assert res.shape == expect_shape