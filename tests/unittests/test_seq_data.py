import numpy as np
import pandas as pd
from unittest import TestCase

from seq_data.root_data import RootData
from seq_data.seq_data import SeqData

from tests.data.constants import *

class TestSeqData(TestCase):

    def test_seq_data(self):
        root = RootData(samples, annot)
        c = SeqData(root)
        assert c.data_names() == []
        assert c.get_node_data('test') == None

        # data: read counts
        c.put_data('RC', df4, root)
        node1 = c.get_node_data('RC')
        assert node1.X.shape == (3, 3)
        df = node1.to_df_samples()
        assert df.shape == (3, 6)
        df = node1.to_df_variables()
        assert df.shape == (7, 3)
        # nodes
        assert root.children == [node1]
        assert node1.parent == root
        assert list(c.nodes) == ['RC', ]
        assert c.data_names() == ['RC']
        # add sample
        sample = pd.Series([3,40], index=['gene1', 'gene3'])
        sample.name = 'sample4'
        node1.put_data(sample)
        # to_df
        df = c.to_df('RC', 0)
        assert df.shape == (4, 6)
        df = c.to_df('RC', 1)
        assert df.shape == (8, 3)

        # statistics
        

        # log of RC
        logdf = np.log1p(node1.X)
        node2 = c.put_data('logRC', logdf, 'RC')
        assert list(c.nodes) == ['RC', 'logRC']
        assert node1.children == [node2,]
        print(logdf)