'''
'''

import pandas as pd

from .stat_data import StatData
from .root_data import RootData
from .node_data import NodeData


class SeqData:
    nodes = {}

    def __init__(self, samples:pd.DataFrame=None, variables:pd.DataFrame=None):
        self.root = RootData(samples, variables)
    
    def data_names(self) -> list:
        return list(self.nodes)
    
    def get_data(self, data_name:str) -> NodeData:
        return self.nodes.get(data_name)
    
    def to_df(self, data_name:str) -> pd.DataFrame:
        if data_name in self.nodes:
            return self.nodes[data_name].to_df()
        return None

    def put_data(self, name:str, X:pd.DataFrame, parent_name:str) -> bool:
        '''
        create/update node data
        '''        
        parent = self.nodes[parent_name] if parent_name in self.nodes \
            else self.nodes['root']
        new_data = NodeData(name, X, parent)
        self.nodes[name] = new_data