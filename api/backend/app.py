from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 1200.99, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 699.99, "category": "Electronics"},
    {"id": 3, "name": "Table", "price": 150.00, "category": "Furniture"},
    {"id": 4, "name": "Chair", "price": 85.50, "category": "Furniture"},
    {"id": 5, "name": "Headphones", "price": 199.99, "category": "Accessories"}
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
