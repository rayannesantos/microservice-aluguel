# UC01–Cadastrar Ciclista
from unittest.mock import Mock


def cadastrar_ciclista(data):
    
    response_mock = Mock()
    response_mock.status_code = "Dados cadastrados", 200

    validacao = True
    if validacao == False:
        response_mock.status_code = 422
        response_mock.json.return_value = [{
            "codigo": 422,
            "mensagem": "Dados inválidos"
        }]
        return response_mock.json()

    validar_cartao()
        
    response_mock.json.return_value = dados_ciclista(data)
    enviar_email()
    return response_mock.json()

def dados_ciclista(data):
    nome =  data.get("ciclista").get("nome")
    nascimento = data.get("ciclista").get("nascimento")
    cpf = data.get("ciclista").get("cpf")
    passaporte_numero = data.get("ciclista").get("passaporte").get("numero")
    passaporte_validade =  data.get("ciclista").get("passaporte").get("validade")
    passaporte_pais =  data.get("ciclista").get("passaporte").get("pais")
    nacionalidade = data.get("ciclista").get("nacionalidade")
        
    email = data.get("ciclista").get("email")
    url_foto_documento = data.get("ciclista").get("url_foto_documento")
    senha = data.get("ciclista").get("senha")
    nome_titular = data.get("meio_de_pagamento").get("nome_titular")
    numero_cartao = data.get("meio_de_pagamento").get("numero")
    validade_cartao = data.get("meio_de_pagamento").get("validade")
    cvv = data.get("meio_de_pagamento").get("cvv")

    mock_json = {
        "ciclista": {
            "id_ciclista": 3,
            "nome": nome,
            "nascimento": nascimento,
            "cpf": cpf,
            "passaporte": {
                "numero": passaporte_numero,
                "validade": passaporte_validade,
                "pais": passaporte_pais
            },
            "nacionalidade": nacionalidade,
            "email": email,
            "url_foto_documento": url_foto_documento,
            "senha": senha
        },
        "meio_de_pagamento": {
            "nome_titular": nome_titular,
            "numero": numero_cartao,
            "validade": validade_cartao,
            "cvv": cvv
        }
    }
    return mock_json


# UC02 – Confirmar email
def ativar_ciclista (id_ciclista):
    response_mock = Mock()
    response_mock.status_code = 200
   
    ciclistas = listar_ciclistas()
    for ciclista in ciclistas:
        if ciclista['id_ciclista'] == id_ciclista:
            ciclista['status'] = 'ativado'
            return ciclista

    return {'error': 'Ciclista not found'}, 404
    


def listar_ciclistas():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = [
       {
        "id_ciclista": 1,
        "status": "desativado",
        "nome": "string",
        "nascimento": "2023-11-13",
        "cpf": "00964211258",
        "passaporte": {
            "numero": "string",
            "validade": "2023-11-13",
            "pais": "JF"
        },
        "nacionalidade": "string",
        "email": "user@example.com",
        "urlFotoDocumento": "string"
        },   
      {
        "id_ciclista": 2,
        "status": "desativado",
        "nome": "string",
        "nascimento": "2023-11-13",
        "cpf": "00964211258",
        "passaporte": {
            "numero": "string",
            "validade": "2023-11-13",
            "pais": "JF"
        },
        "nacionalidade": "string",
        "email": "user@example.com",
        "urlFotoDocumento": "string"
      },   
    ]
    return response_mock.json()


# método de enviar email (retornando sempre "sucesso"), mas que não chame o microsserviço Externo. 
def enviar_email():
    response_mock = Mock()
    response_mock.json.return_value = {"message": "Email enviado com sucesso"}
    return response_mock.json()

# Apenas para retornar sem chamar o microsserviço externo
def validar_cartao():
    return True