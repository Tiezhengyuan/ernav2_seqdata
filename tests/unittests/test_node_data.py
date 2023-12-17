from unittest import TestCase, mock
from ddt import ddt, data, unpack
from seq_data.node_data import NodeData

from tests.data.constants import *


@ddt
class TestNodeData(TestCase):

    @data(
        [None, 'root'],
        ['new', 'new'],
    )
    @unpack
    def test_name(self, name, expect):
        c = NodeData(name)
        assert c.name == expect

    @data(
        [None, (0, 0)],
        [df1, (3, 3)],
        [s1, (3,1)],
        [l1, (3,1)],
    )
    @unpack
    def test_X(self, X, expect):
        c = NodeData(None, X)
        print(c.X.shape)
