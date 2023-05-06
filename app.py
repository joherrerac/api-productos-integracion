from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "lista de productos musicales"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message": "producto agregado", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quanitity'] = request.json['quanitity']
        
        return jsonify({
            "message": "producto actualizado",
            "product": productFound[0]
        })
    return jsonify({"message": "product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound)[0]
        return jsonify({
            "message": "product deleted",
            "product": products
        })
    return jsonify({"message": "product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)