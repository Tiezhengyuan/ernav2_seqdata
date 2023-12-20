from unittest import TestCase, mock
from ddt import ddt, data, unpack

from seq_data.root_data import RootData
from seq_data.node_data import NodeData

from tests.data.constants import *


@ddt
class TestNodeData(TestCase):
    @data(
        ['new', 'new'],
    )
    @unpack
    def test_name(self, name, expect):
        c = NodeData(RootData(), name)
        assert c.name == expect

    @data(
        [None, (0, 0)],
        [df1, (3, 3)],
        [s1, (3,1)],
        [l1, (3,1)],
    )
    @unpack
    def test_X(self, X, expect_shape):
        c = NodeData(RootData(), 'test', X)
        assert c.X.shape == expect_shape

    def test_default_node(self):
        c = NodeData(RootData(), 'test', df4)

        # row names and column names
        assert c.name == 'test'
        assert c.X.shape == (3,3)
        assert list(c.X.index) == ['sample1', 'sample2', 'sample3']
        assert list(c.X) == ['gene1', 'gene2', 'gene3']

        res = c.row_labels()
        assert list(res) == []
        assert list(res.index) == ['sample1', 'sample2', 'sample3']

        res = c.col_labels()
        assert list(res) == ['gene1', 'gene2', 'gene3']
        assert list(res.index) == []

    def test_put_data(self):
        c = NodeData(RootData(), 'test', df4)

        s = pd.Series([0, 10, 212], index=['gene3', 'gene1', 'gene2'])
        s.name = 'sample4'
        c.put_data(s)
        assert list(c.X)== ['gene1', 'gene2', 'gene3']
        assert list(c.X.loc['sample1']) == list(df4.loc['sample1'])
        assert list(c.X.loc['sample4']) == [10., 212., 0.]

        # different columns
        s = pd.Series([10, 21, 2], index=['gene4', 'gene1', 'gene2'])
        s.name = 'sample5'
        c.put_data(s)
        assert list(c.X)== ['gene1', 'gene2', 'gene3', 'gene4']
        assert list(c.X.loc['sample1']) == [23., 10., 0., 0.]
        assert list(c.X.loc['sample5']) == [21., 2., 0., 10.]

        # update
        s = pd.Series([10, 20], index=['gene1', 'gene2'])
        s.name = 'sample5'
        c.put_data(s)
        assert list(c.X.loc['sample5']) == [31., 22., 0., 10.]

    def test_row_labels(self):
        # root data is empty
        c = NodeData(RootData(), 'test', df4)

        # add row/column
        s = pd.Series([10, 21, 2], index=['gene4', 'gene1', 'gene2'])
        c.put_data(s)
        labels = c.row_labels()
        assert list(labels) == []
        assert list(labels.index) == ['sample1', 'sample2', 'sample3', 4]

        # missing data
        s = pd.Series(None, index=['gene1', 'gene2'])
        c.put_data(s)
        labels = c.row_labels()
        assert list(labels) == []
        assert list(labels.index) == ['sample1', 'sample2', 'sample3', 4, 5]

        # sample info and annotations
        c = NodeData(RootData(samples, annot), 'test', df4)

        # add row/column
        s = pd.Series([10, 21, 2], index=['gene4', 'gene1', 'gene2'])
        c.put_data(s)

        labels = c.row_labels()
        assert labels.shape == (4,3)
        assert list(labels) == ['sample_name', 'age', 'gender']
        assert list(labels.index) == ['sample1', 'sample2', 'sample3', 4]

        labels = c.row_labels(['sample_name', 'age', 'gender'])
        assert labels.shape == (4,3)
        assert list(labels) == ['sample_name', 'age', 'gender']
        assert list(labels.index) == ['sample1', 'sample2', 'sample3', 4]

        labels = c.row_labels(['gender', 'XXX',])
        assert labels.shape == (4,2)
        assert list(labels) == ['gender', 'XXX',]
        assert list(labels.index) == ['sample1', 'sample2', 'sample3', 4]
