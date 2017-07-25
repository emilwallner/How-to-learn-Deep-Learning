import pandas as pd
import numpy as np

def clean_data(data):
    data["Age"].fillna(data["Age"].mean(), inplace=True)
    data.drop(data.columns[[0, 2, 7, 9]], axis=1, inplace=True)
    data = pd.get_dummies(data, columns=['Sex' , 'Embarked', 'Pclass'], drop_first=True)
    return np.array(data, dtype=np.float32)
