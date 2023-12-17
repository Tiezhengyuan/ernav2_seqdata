'''
Given a sample or observance,
Names of variables or features or lables in different scenario
'''
import pandas as pd


class ColLabels:
    def __init__(self, data:pd.DataFrame=None, labels:list=None) -> None:
        '''
        data: pd.DataFrame, list
        Note: column names must be unique
        '''
        self.data = data if data else pd.DataFrame(None)
        if labels:
            self.data.columns = labels
    
    def labels(self):
        '''
        column names
        '''
        return list(self.data)