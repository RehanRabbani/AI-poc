import pandas as pd
from app.models import model
from app.utils import load_data

# Load the dataset
df = load_data()

# Create a pivot table for the User-Product interaction matrix
user_product_matrix = df.pivot_table(index='User', columns='ProductID', values='Rating', fill_value=0)

def recommend_products(user_idx, num_recommendations=3):
    distances, indices = model.kneighbors(user_product_matrix.iloc[user_idx:user_idx+1], n_neighbors=num_recommendations)

    # Get products rated by the similar users
    similar_users_ratings = user_product_matrix.iloc[indices[0]]

    # Average ratings for the products across similar users
    avg_ratings = similar_users_ratings.mean(axis=0)
    
    # Sort products by rating
    recommended_products = avg_ratings.sort_values(ascending=False)
    
    # Return top recommended products
    return recommended_products.head(num_recommendations)
