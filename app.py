# Seu código aqui
from flask import Flask, request, jsonify
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
        data["id"] = len(produtos)
        new_product = data.get('name')
        produtos.append(data)
        print(data)
        return {'message': f"O Produto {new_product} foi adcionado em estoque!"}, 201

    elif request.method == 'GET':
        return jsonify(produtos), 200

@app.route('/products/<int:product_id>', methods=['GET',"PATCH","PUT","DELETE"])
def update(product_id: int):
    quantidade_de_produtos = len(produtos)
    
    if request.method == "PATCH" or request.method == "PUT":
        for product in produtos:
            if quantidade_de_produtos < product_id or product_id < 1:
                return {'message': 'Produto não existe'}

            elif product_id == product['id']:
                data= request.get_json()
                product['name'] =data['name']
                return jsonify(), 204   


    elif request.method == 'GET':
        for product in produtos:
            if quantidade_de_produtos < product_id or product_id < 1:
                return {'message': 'Produto não existe'}

            elif product_id == product['id']:
                product = [product]
                return jsonify(product), 200


    elif request.method == 'DELETE':
        for indice, product in enumerate(produtos):
            if quantidade_de_produtos < product_id or product_id < 1:
                return {'message': 'Produto não existe'}

            elif product_id == product['id']:
                del produtos[indice]
                return jsonify(), 204
