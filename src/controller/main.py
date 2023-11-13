import requests, os, sys
from flask import Flask
from flask import Flask, request

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.CiclistaService import cadastrar_ciclista
from service.FuncionarioService import listar_funcionarios
app = Flask(__name__)


# CICLISTAS
@app.route('/ciclista', methods=['POST'])
def cadastrar_ciclista_route():
        data = request.get_json()
        nome =  data.get("ciclista", {}).get("nome")
        nascimento = data.get("ciclista", {}).get("nascimento")
        cpf = data.get("ciclista", {}).get("cpf")
        passaporteNumero = data.get("ciclista", {}).get("passaporte", {}).get("numero")
        passaporteValidade =  data.get("ciclista", {}).get("passaporte", {}).get("validade")
        passaportePais =  data.get("ciclista", {}).get("passaporte", {}).get("pais")
        nacionalidade = data.get("ciclista", {}).get("nacionalidade")
        
        email = data.get("ciclista", {}).get("email")
        urlFotoDocumento = data.get("ciclista", {}).get("urlFotoDocumento")
        senha = data.get("ciclista", {}).get("senha")
        nomeTitular = data.get("meioDePagamento", {}).get("nomeTitular")
        numeroCartao = data.get("meioDePagamento", {}).get("numero")
        validadeCartao = data.get("meioDePagamento", {}).get("validade")
        cvv = data.get("meioDePagamento", {}).get("cvv")
        
    
        response = cadastrar_ciclista(nome, nascimento,cpf, passaporteNumero, passaporteValidade, passaportePais, nacionalidade,
                                      email,urlFotoDocumento,senha, nomeTitular, numeroCartao, validadeCartao, cvv)

        return response


# FUNCIONARIOS 

@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios_route():
    funcionarios = listar_funcionarios()
    return funcionarios

if __name__ == '__main__':
    app.run(debug=True)