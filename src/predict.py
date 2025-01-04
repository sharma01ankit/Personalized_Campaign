import pandas as pd

def predict_customers(model, new_data):
    predictions = model.predict(new_data)
    return predictions
