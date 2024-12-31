from flask import jsonify
from app import app
from app.recommendation import recommend_products

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    recommended_products = recommend_products(user_id - 1)  # Adjust for 0-based indexing
    return jsonify(recommended_products.to_dict())
