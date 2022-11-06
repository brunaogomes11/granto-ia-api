from app.iaModel import predict
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def servidorLigado():
    return "Servidor Rodando"

@app.route("/testar/<genero>/<idade>/<debito>/<casado>/<contaBanco>/<tipo_industria>/<etnia>/<anos_empregado>/<inadimplenia>/<empregado>/<pont_credito>/<cnh>/<cidadania>/<cep>/<renda>", methods=["GET"])
def criarModelos(genero, idade, debito, casado, contaBanco, tipo_industria, etnia, anos_empregado, inadimplencia, empregado, pont_credito, cnh, cidadania, cep, renda):
    if request.data:
        dados = [genero, idade, debito, casado, contaBanco, tipo_industria, etnia, anos_empregado, inadimplencia, empregado, pont_credito, cnh, cidadania, cep, renda]
        aprovado = predict(dados)
        return jsonify({'Aprovado':f'{aprovado}'}) 

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
