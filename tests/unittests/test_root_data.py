from copy import deepcopy
from unittest import TestCase, mock
from ddt import ddt, data, unpack

from seq_data.root_data import RootData

from tests.data.constants import samples, annot


@ddt
class TestRootData(TestCase):

    def test_init(self):
        root = RootData()
        assert root.samples.axis == 0
        assert len(root.samples.data) == 0
        assert len(root.variables.data) == 0
        assert root.is_root == True

        root = RootData(samples, annot)
        assert list(root.samples.data.index) == ['sample1', 'sample2']
        assert list(root.variables.data.index) == ['gene1', 'gene2']
        assert root.is_root == True