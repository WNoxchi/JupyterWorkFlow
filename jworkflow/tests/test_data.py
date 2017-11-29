from jworkflow.data import get_fremont_data
import pandas as pd
import numpy as np

def test_fremont_data():
    data = get_fremont_data()
    # we know data.columns should be west east & total:
    assert all(data.columns == ['West', 'East', 'Total'])
    # also want date.index to be a DateTimeIndex instance
    assert isinstance(data.index, pd.DatetimeIndex)
    # make sure data has 12-hour columns: check for 24 unique hours (?)
    assert len(np.unique(data.index.time) == 24)
