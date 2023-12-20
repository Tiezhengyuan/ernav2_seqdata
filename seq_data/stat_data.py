
'''
One set of data shall include many samples.
One sample may contain many variables or features
'''
import pandas as pd

class StatData:
    def __init__(self, axis:int=None) -> None:
        '''
        data: dict
        Note: index/column names must be unique
        '''
        self.axis = 1 if axis else 0
        self.data = {}

    def put(self, name:str, input:pd.Series=None):
        '''
        update or create
        '''
        _data = pd.Series(None, dtype='float') if input is None else pd.Series(input)
        _data.name = name
        self.data[name] = _data

    def to_df(self, names:list=None, labels:list=None):
        '''
        export colData as dataframe
        '''
        if not self.data:
            return pd.DataFrame(None, dtype='float')
        
        _data = [self.data[i] for i in names if i in self.data and not self.data[i].empty] \
            if names else [v for v in self.data.values() if not v.empty]
        df = pd.concat(_data, axis=1)
        if labels:
            df = df.reindex(labels)
        if self.axis == 1:
            return df.fillna(0).transpose()
        return df.fillna(0)


    
