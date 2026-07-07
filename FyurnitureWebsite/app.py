import os
from flask import Flask, render_template, abort

app = Flask(__name__)

# =====================================================
# PRODUCT DATA
# =====================================================

products = {

    "SF101": {
        "id": "SF101",
        "category": "sofas",
        "name": "Luxury Wooden Sofa",
        "price": "₹24,999",
        "material": "Teak Wood",
        "colour": "Walnut Brown",
        "dimensions": "210 x 90 x 85 cm",
        "availability": "In Stock",
        "description": "Premium handcrafted wooden sofa designed for modern homes.",
        "image": "https://indiannest.in/cdn/shop/files/H598fb849e1e543528cc6e61987f27a47u.jpg?v=1684257622"
    },

    "SF102": {
        "id": "SF102",
        "category": "sofas",
        "name": "Modern L Shape Sofa",
        "price": "₹39,999",
        "material": "Engineered Wood",
        "colour": "Grey",
        "dimensions": "260 x 180 x 85 cm",
        "availability": "In Stock",
        "description": "Modern L-shaped sofa perfect for spacious living rooms.",
        "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=900&q=80"
    },

    "CH101": {
        "id": "CH101",
        "category": "chairs",
        "name": "Luxury Chair",
        "price": "₹7,999",
        "material": "Oak Wood",
        "colour": "Brown",
        "dimensions": "60 x 60 x 95 cm",
        "availability": "In Stock",
        "description": "Comfortable premium wooden chair.",
        "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80"
    }

}


# =====================================================
# HOME
# =====================================================

@app.route("/")
def welcome():

    return render_template("welcome.html")


# =====================================================
# HOME PAGE
# =====================================================

@app.route("/home")
def home():

    return render_template("home.html")


# =====================================================
# CATEGORY PAGE
# =====================================================

@app.route("/category/<category_name>")
def category(category_name):

    category_products = []

    for product in products.values():

        if product["category"] == category_name:

            category_products.append(product)

    return render_template(

        "category.html",

        category=category_name.title(),

        products=category_products

    )


# =====================================================
# PRODUCT DETAILS
# =====================================================

@app.route("/product/<product_id>")
def product(product_id):

    product = products.get(product_id)

    if product is None:

        abort(404)

    return render_template(

        "product.html",

        product=product

    )

# =====================================================
# RUN APP
# =====================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )