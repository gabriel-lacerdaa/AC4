from flask import Flask, jsonify, request
import requests
app = Flask(__name__)


@app.route('/venda/produtos')
def novaVenda():
    id = request.args.get("id")
    response = requests.get(f'http://localhost:5000/produtos/{id}')
    return response.json()

    
@app.route('/cadastrar/produto', methods=["POST"])
def cadastrarProduto():
    dadosJson = request.get_json()
    nome_produto = dadosJson["nome"]
    preco_produto = dadosJson["preco"]
    response = requests.post(f"http://localhost:5000/produtos/cadastrar?nome={nome_produto}&preco={preco_produto}")
    return  response.json()

@app.route('/deletar/produto', methods=["DELETE"])
def deletarProduto():
    id = request.args.get("id")
    response = requests.delete(f'http://localhost:5000/produtos/deletar?id={id}')
    return response.json()
        

if __name__ == "__main__":
    app.run(host="localhost",port=3000, debug=True)
