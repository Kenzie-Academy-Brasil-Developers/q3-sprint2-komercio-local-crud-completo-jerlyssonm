# Seu código aqui
from flask import Flask, json, request, jsonify
from produtos_db import produtos

app = Flask(__name__)

@app.get('/')
def greeting():
    message = {"message": "Entrega 5 - Komercio Local"}
    return message

@app.route('/products', methods=['POST','GET'])
def list_products():
    if request.method == 'POST':
        data = request.get_json()
        new_product = data.get('name')
        produtos.append(data)
        return {'message': f"O Produto {new_product} foi adcionado em estoque!"}, 201
    elif request.method == 'GET':
        return jsonify(produtos), 200

@app.get("/products/<int:product_id>")
def get(product_id: int):
    quantidade_de_produtos = len(produtos)
    for x in produtos:
        if quantidade_de_produtos < product_id or product_id < 1:
            return {'message': 'Produto não existe'}
        elif product_id == x['id']:
            x = [x]
            return jsonify(x), 200

@app.route('/products/<int:product_id>', methods=["PATCH","PUT"])
def update(product_id: int):
    quantidade_de_produtos = len(produtos)
    for x in produtos:
        if quantidade_de_produtos < product_id or product_id < 1:
            return {'message': 'Produto não existe'},204
        elif product_id == x['id']:
            data= request.get_json()
            x['name'] =data['name']
            return jsonify(), 204   

@app.delete('/products/<int:product_id>')
def delete(product_id):
    quantidade_de_produtos = len(produtos)
    for indice, product in enumerate(produtos):
        if quantidade_de_produtos < product_id or product_id < 1:
            return {'message': 'Produto não existe'},204
        elif product_id == product['id']:
            del produtos[indice]
            return jsonify(), 204      