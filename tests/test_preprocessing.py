import pandas as pd
from src.data_preprocessing import preprocess_data

def test_preprocess_data():
    data = pd.DataFrame({
        'recency': [10, 20, 1000],
        'frequency': [5, 50, 500],
        'monetary': [100, 2000, 10000]
    })
    processed_data = preprocess_data(data)
    assert processed_data['recency'].max() <= 3
    assert processed_data['frequency'].min() >= -3
