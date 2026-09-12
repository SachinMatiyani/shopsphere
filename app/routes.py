from flask import Blueprint, jsonify, request
from app.models import Product
from app.extensions import db

main = Blueprint("main", __name__)

@main.route("/")
def homepage():
    return "Hello World"

@main.route("/api/products", methods=["GET", "POST"])
def products():
    if request.method == "POST":
        data = request.get_json()
        if data is None:
            return "Invalid Request!"
        if "name" not in data:
            return "name is missing!"
        if "price" not in data:
            return "price is missing!"
        if not isinstance(data["price"], int):
            return "price must be an integer!"
        
        product = Product(name=data["name"], price=data["price"])
        db.session.add(product)
        db.session.commit()
        
        return jsonify({"message": "Product has successfully been added!"})
    else:
        products = Product.query.all()
        product_list = []

        for product in products:
            product_list.append({
                "id": product.id,
                "name": product.name,
                "price": product.price
            })
        return jsonify(product_list)