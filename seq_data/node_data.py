'''
independent data in matrix
samples in rows, variables in columns
'''
import pandas as pd

from .col_labels import ColLabels
from .row_labels import RowLabels

class NodeData:
    def __init__(self, name:str=None, X:pd.DataFrame=None, parent=None):
        self.name = name if name else 'root'
        self.X = pd.DataFrame(X) if X is not None else pd.DataFrame(None)
        # 
        col_labels = parent.variables.labels() if parent else list(self.X)
        self.variables = ColLabels(col_labels)
        row_labels = parent.samples.labels() if parent else list(self.X.index)
        self.samples = RowLabels(row_labels)
        # tree structure
        self.parent = None

    def get_root(self):
        if self.parent:
            return self.parent.get_root()
        return self
    
    def col_labels(self) -> pd.DataFrame:
        root = self.get_root()
        col_labels = pd.concat([root.col_labels, self.col_labels], axis=0)
        return col_labels

    def row_labels(self) -> pd.DataFrame:
        root = self.get_root()
        row_labels = pd.concat([root.row_labels, self.row_labels], axis=1)
        return row_labels

    def to_df(self) -> pd.DataFrame:
        return self.X

    def add_data(self, new_data):
        self.X = pd.concat([self.X, new_data], axis=0)
