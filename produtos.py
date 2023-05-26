from flask import Flask, jsonify, request
from conexaoBD import cursor, conn

app = Flask(__name__)

cursor.execute('USE Produtos;')


@app.route('/produtos')
def TodosProdutos():
    cursor.execute(f'SELECT * FROM Produtos;')
    produtos = cursor.fetchall()
    produtos_json = []
    for produto in produtos:
        produto_dict = {
            'id': produto[0],
            'nome': produto[1],
            'preco': float(produto[2])
        }
        produtos_json.append(produto_dict)
    return jsonify(produtos_json)

from flask import jsonify, request

@app.route('/produtos/<int:id>')
def produtoPorid(id):
    cursor.execute(f'SELECT * FROM Produtos WHERE id = {id}')
    produto = cursor.fetchone()
    if not produto:
        return jsonify({'mensagem': 'Produto não encontrado.'}), 404
    produto_dict = {
        'id': produto[0],
        'nome': produto[1],
        'preco': float(produto[2])
    }
    return jsonify(produto_dict), 200



@app.route('/produtos/cadastrar', methods=["POST"])
def cadastrarProduto():
    nome = request.args.get("nome")
    preco = float(request.args.get("preco"))
    sql = '''
    INSERT INTO Produtos(nome, preco)
    values (%s, %s)
    '''
    try:
        cursor.execute(sql, (nome,preco))
        print('paradinha1')
        conn.commit()
        print('paradinha2')
        return jsonify({"mensagem":"produto inserido com sucesso"}), 201
    except:
        return "Erro ao inserir", 400



@app.route("/produtos/deletar", methods=["DELETE"])
def deletarProduto():
    id = request.args.get("id")
    cursor.execute(f'SELECT * FROM Produtos where id = {id}')
    respost = cursor.fetchone()
    if not respost:
        return jsonify({"mensagem": f"Não foi encontrado produto com id {id}"}), 404 
    sql = f'DELETE FROM Produtos WHERE id = {id}'
    cursor.execute(sql)
    conn.commit()
    return jsonify({"mensagem": f"produto com id {id} foi deletado"}), 200


if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=5000)
