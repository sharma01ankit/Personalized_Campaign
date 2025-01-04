import numpy as np

def segment_customers(data):
    conditions = [
        (data['recency'] < -0.5),
        (data['frequency'] > 0.5),
        (data['monetary'] > 0.5)
    ]
    choices = ['High', 'Medium', 'Low']
    data['RFM_Segment'] = np.select(conditions, choices, default='Low')
    return data
