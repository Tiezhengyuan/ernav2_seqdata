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

    
    @data(
        [None, None, (3, 4), list('ABC'), list('abcd')],
        [None, list('abcf'), (3, 4), list('ABC'), list('abcf')],
        [['A'], list('abc'), (1, 3), ['A'], list('abc')],
        [['A'], list('bca'), (1, 3), ['A'], list('bca')],
        [['A','E'], list('abc'), (2, 3), ['A', 'E'], list('abc')],
        [['B',], None, (1, 4), ['B'], list('bcad')],
    )
    @unpack
    def test_to_df_row(self, names, labels, expect_shape, \
            expect_row, expect_col):
        c = StatData(0)
        c.put('A', s1)
        c.put('B', s2)
        c.put('C')
        res = c.to_df(names, labels)
        assert res.shape == expect_shape
        assert list(res) == expect_col
        assert list(res.index) == expect_row


    @data(
        [None, None, (4, 3), list('abcd'), list('ABC')],
        [None, list('abcf'), (4, 3), list('abcf'), list('ABC')],
        [['A'], list('abc'), (3, 1), list('abc'), ['A']],
        [['A'], list('bca'), (3, 1), list('bca'), ['A']],
        [['A','E'], list('abc'), (3, 2), list('abc'), list('AE')],
        [['B'], None, (4,1), list('bcad'), ['B']],
    )
    @unpack
    def test_to_df_col(self, names, labels, expect_shape, \
            expect_row, expect_col):
        c = StatData(1)
        c.put('A', s1)
        c.put('B', s2)
        c.put('C')
        res = c.to_df(names, labels)
        assert res.shape == expect_shape
        assert list(res) == expect_col
        assert list(res.index) == expect_row
    
    @data(
        [0, None, None, (0,0)],
        [0, ['sample1'], None, (0,0)],
        [1, None, None, (0,0)],
        [1, ['gene1'], None, (0,0)],
    )
    @unpack
    def test_to_df_empty(self, axis, key1, key2, expect_shape):
        c = StatData(axis)
        res = c.to_df(key1, key2)
        assert res.shape == expect_shape
