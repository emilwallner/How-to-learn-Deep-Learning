import pandas as pd
import numpy as np

def clean_data(data):
    data["Age"].fillna(data["Age"].mean(), inplace=True)
    data.drop(data.columns[[0, 2, 7, 9]], axis=1, inplace=True)
    data.replace(['male', 'female'], [1, 2], inplace=True)
    data.replace(['S', 'C', 'Q', np.nan], [1, 2, 3, 0], inplace=True)
    return data
