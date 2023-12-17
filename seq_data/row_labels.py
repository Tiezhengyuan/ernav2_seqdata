
'''
One set of data shall include many samples.
One sample may contain many variables or features
'''
import pandas as pd


class RowLabels:
    def __init__(self, data:pd.DataFrame=None, labels:list=None) -> None:
        '''
        data: pd.DataFrame, list
        Note: index must be unique
        '''
        self.data = data if data else pd.DataFrame(None)
        if labels:
            self.data.index = labels

    def labels(self):
        '''
        '''
        return self.data.index
    
    
