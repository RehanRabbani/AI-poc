from sklearn.neighbors import NearestNeighbors
from app.utils import load_data

# Load the dataset
df = load_data()

# Create a pivot table for the User-Product interaction matrix
user_product_matrix = df.pivot_table(index='User', columns='ProductID', values='Rating', fill_value=0)

# Train a KNN model to find similar users
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(user_product_matrix)
