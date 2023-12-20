'''
independent data in matrix
samples in rows, variables in columns
'''
import pandas as pd
import json

from .stat_data import StatData
from .root_data import RootData


class NodeData:
    is_root = False

    def __init__(self, parent:RootData, name:str, X:pd.DataFrame=None):
        self.parent = parent
        self.name = name
        self.X = pd.DataFrame(X, dtype='float')
        # cross row
        self.samples = parent.samples
        self.row_stat = StatData(axis=0)
        # cross columns
        self.variables = parent.variables
        self.col_stat = StatData(axis=1)

    def get_root(self):
        if self.parent:
            return self.parent.get_root()
        return self

    def row_labels(self, labels:list=None) -> pd.DataFrame:
        key1 = list(self.X.index)
        _annot = self.samples.to_df(key1, labels)
        _stat = self.row_stat.to_df(key1, labels)
        return pd.concat([_annot, _stat], axis=1).fillna('-')

    def col_labels(self, labels:list=None) -> pd.DataFrame:
        key1 = list(self.X)
        _var = self.variables.to_df(key1, labels)
        _stat = self.col_stat.to_df(key1, labels)
        return pd.concat([_var, _stat], axis=0).fillna('-')

    def put_data(self, new_data:pd.Series):
        '''
        index names of series are columns names
        '''
        if not new_data.name:
            new_data.name = self.X.shape[0] + 1
        else:
            if new_data.name in list(self.X.index):
                _data = self.X.loc[new_data.name]
                self.X.loc[new_data.name] = NodeData.combine_series(
                    self.X.loc[new_data.name], new_data
                )
                return self.X.loc[new_data.name]
        _data = pd.DataFrame(new_data).T
        self.X = pd.concat([self.X, _data], axis=0).fillna(0)
        return self.X.loc[new_data.name]

    @staticmethod
    def combine_series(s1:pd.Series, s2:pd.Series) -> pd.Series:
        def func(x, y):
            _x = 0 if str(x) == 'nan' else x
            _y = 0 if str(y) == 'nan' else y
            return _x + _y
        return s1.combine(s2, func)

    def to_df(self, row_label_names:list=None, col_label_names:list=None):
        row_data = self.row_labels(row_label_names)
        _data = pd.concat([row_data, self.X], axis=1) if row_data else self.X