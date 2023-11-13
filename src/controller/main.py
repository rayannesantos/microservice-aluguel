import requests, os, sys
from flask import Flask
from flask import Flask, request

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from service.CiclistaService import cadastrar_ciclista, listar_ciclistas,ativar_ciclista
from service.FuncionarioService import listar_funcionarios, cadastrar_funcionario, editar_funcionario, remover_funcionario
app = Flask(__name__)


# CICLISTAS
@app.route('/ciclista', methods=['POST'])
def cadastrar_ciclista_route():
        data = request.get_json()
        nome =  data.get("ciclista", {}).get("nome")
        nascimento = data.get("ciclista", {}).get("nascimento")
        cpf = data.get("ciclista", {}).get("cpf")
        passaporte_numero = data.get("ciclista", {}).get("passaporte", {}).get("numero")
        passaporte_validade =  data.get("ciclista", {}).get("passaporte", {}).get("validade")
        passaporte_pais =  data.get("ciclista", {}).get("passaporte", {}).get("pais")
        nacionalidade = data.get("ciclista", {}).get("nacionalidade")
        
        email = data.get("ciclista", {}).get("email")
        url_foto_documento = data.get("ciclista", {}).get("urlFotoDocumento")
        senha = data.get("ciclista", {}).get("senha")
        nome_titular = data.get("meioDePagamento", {}).get("nomeTitular")
        numero_cartao = data.get("meioDePagamento", {}).get("numero")
        validade_cartao = data.get("meioDePagamento", {}).get("validade")
        cvv = data.get("meioDePagamento", {}).get("cvv")
        
    
        response = cadastrar_ciclista(nome, nascimento,cpf, passaporte_numero, passaporte_validade, passaporte_pais, nacionalidade,
                                      email,url_foto_documento,senha, nome_titular, numero_cartao, validade_cartao, cvv)

        return response



@app.route('/ciclista/<int:id_ciclista>/ativar', methods=['POST'])
def ativar_ciclista_route(id_ciclista):
    response = ativar_ciclista(id_ciclista)
    return response


@app.route('/ciclistas', methods=['GET'])
def listar_ciclistas_route():
    ciclistas = listar_ciclistas()
    return ciclistas



# FUNCIONARIOS 

@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios_route():
    funcionarios = listar_funcionarios()
    return funcionarios


@app.route('/funcionario', methods=['POST'])
def cadastrar_funcionario_route():
        data = request.get_json()
        senha = data.get("senha")
        confirmacao_senha = data.get("confirmacaoSenha")
        email =  data.get("email")
        nome = data.get("nome")
        idade = data.get("idade")
        funcao = data.get("funcao")
        cpf = data.get("cpf")

        response = cadastrar_funcionario(senha,confirmacao_senha,email, nome, idade,funcao,cpf)
        return response


@app.route('/funcionario/<int:id_funcionario>', methods=['PUT'])
def editar_funcionario_route(id_funcionario):
        data = request.get_json()
        senha = data.get("senha")
        confirmacao_senha = data.get("confirmacaoSenha")
        email =  data.get("email")
        nome = data.get("nome")
        idade = data.get("idade")
        funcao = data.get("funcao")
        cpf = data.get("cpf")

        response = editar_funcionario(id_funcionario,senha,confirmacao_senha,email, nome, idade,funcao,cpf)
        return response
    

@app.route('/funcionario/<int:id_funcionario>', methods=['DELETE'])
def remover_funcionario_route(id_funcionario):
        response = remover_funcionario(id_funcionario)
        return response
    


if __name__ == '__main__':
    app.run(debug=True)