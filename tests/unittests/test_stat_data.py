from unittest import TestCase, mock
from ddt import ddt, data, unpack
from seq_data.stat_data import StatData

from tests.data.constants import *


@ddt
class TestStatData(TestCase):

    def test_put(self):
        c = StatData()
        c.put('a')
        assert c.data['a'].name == 'a'
        assert c.data['a'].shape == (0,)

        c.put('b', s1)
        assert c.data['b'].shape == (3,)
        assert list(c.data) == ['a', 'b']

        c.put('a', s2)
        assert c.data['a'].shape == (4,)
        assert list(c.data) == ['a', 'b']

    '''
    @data(
        [None, None, (4,2), list('abcd')],
        [None, list('abcf'), (4,2), list('abcf')],
        [['A'], list('abc'), (3,1), list('abc')],
        [['A'], list('bca'), (3,1), list('bca')],
        [['A','E'], list('abc'), (3,1), list('abc')],
        [['B',], None, (4,1), list('bcad')],
    )
    @unpack
    def test_to_df_row(self, names, labels, expect_shape, expect_index):
        c = StatData(0)
        c.put('A', s1)
        c.put('B', s2)
        c.put('C')
        res = c.to_df(names, labels)
        assert res.shape == expect_shape
        assert list(res.index) == expect_index


    @data(
        [None, None, (2,4), list('abcd')],
        [None, list('abcf'), (2,4), list('abcf')],
        [['A'], list('abc'), (1,3), list('abc')],
        [['A'], list('bca'), (1,3), list('bca')],
        [['A','E'], list('abc'), (1,3), list('abc')],
        [['B'], None, (1,4), list('bcad')],
    )
    @unpack
    def test_to_df_col(self, names, labels, expect_shape, expect_columns):
        c = StatData(1)
        c.put('A', s1)
        c.put('B', s2)
        c.put('C')
        res = c.to_df(names, labels)
        assert res.shape == expect_shape
        assert list(res) == expect_columns
    '''
    @data(
        [0, None, None, (0,0)],
        [0, ['sample1'], None, (0,0)],
        [1, None, None, (0,0)],
        [1, ['gene1'], None, (0,0)],
    )
    @unpack
    def test_to_df_empty(self, axis, names, labels, expect_shape):
        c = StatData(axis)
        res = c.to_df(names, labels)
        assert res.shape == expect_shape
