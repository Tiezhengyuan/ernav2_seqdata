'''
'''

import pandas as pd

from .col_labels import ColLabels
from .row_labels import RowLabels
from .node_data import NodeData


class SeqData:
    nodes = {}

    def __init__(self, root_data:NodeData=None):
        self.root = root_data if root_data else NodeData('root')
        self.nodes[self.root.name] = self.root
    
    def data_names(self) -> list:
        return list(self.nodes)
    
    def get_data(self, data_name:str) -> NodeData:
        return self.nodes.get(data_name)
    
    def to_df(self, data_name:str) -> pd.DataFrame:
        if data_name in self.nodes:
            return self.nodes[data_name].to_df()
        return None

