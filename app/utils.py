import pandas as pd

def load_data():
    # Load the dataset
    df = pd.read_csv('data/user_product_ratings.csv')
    return df
