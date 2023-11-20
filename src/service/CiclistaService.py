# Como dito anteriormente, essa camada é responsável por guardar e abstrair as regras de negócio, 
# para que a camada Model seja "leve" e objetiva. Sendo ainda responsável pelo acesso aos dados, 
# validando se as informações recebidas da camada Controllers são suficientes para completar a requisição.
#####################################################################################################
# Centralizar o acesso aos dados e funções externas
# Abstrair regras de negócios
# Não ter nenhum "conhecimento" sobre a camada Model (EX: Query SQL)
# Não receber nada relacionada ao HTTP (Request ou Response)

# UC01–Cadastrar Ciclista
from unittest.mock import Mock
from model.CiclistaModel import Ciclista

class CiclistaService: 
    def __init__(self):
        # Inicializa com alguns dados fictícios de ciclistas
        self.ciclistas_data = [
            {
                "id_ciclista": 3,
                "nome": "Ciclista 1",
                "nascimento": "nascimento",
                "cpf": "cpf",
                "passaporte": {
                    "numero": "passaporte_numero",
                    "validade": "passaporte_validade",
                    "pais": "passaporte_pais"
                },
                "nacionalidade": "nacionalidade",
                "email": "email",
                "url_foto_documento": "url_foto_documento",
                "senha": "senha"
            },
            {
                "id_ciclista": 4,
                "nome": "Ciclista 2",
                "nascimento": "nascimento",
                "cpf": "cpf",
                "passaporte": {
                    "numero": "passaporte_numero",
                    "validade": "passaporte_validade",
                    "pais": "passaporte_pais"
                },
                "nacionalidade": "nacionalidade",
                "email": "email",
                "url_foto_documento": "url_foto_documento",
                "senha": "senha"
            }
        ]
        self.ciclistas = [Ciclista(**ciclista_data) for ciclista_data in self.ciclistas_data]


    def listar_todos(self):
        ciclistas = [ciclista.to_dict() for ciclista in self.ciclistas]
        return ciclistas
        
        
    # UC06 – Alterar Dados do Ciclista
    def alterar_ciclista(self, id_ciclista, dados):
        ciclista = self.obter_ciclista_por_id(id_ciclista)
        email=''
        
        if ciclista:
            # Atualiza os dados do ciclista com os novos dados
            ciclista.nome = dados.get("nome", ciclista.nome)
            ciclista.cpf = dados.get("cpf", ciclista.cpf)
            ciclista.passaporte = dados.get("passaporte", ciclista.passaporte)
            ciclista.nacionalidade = dados.get("nacionalidade", ciclista.nacionalidade)
            ciclista.url_foto_documento = dados.get("url_foto_documento", ciclista.url_foto_documento)
            ciclista.senha = dados.get("senha", ciclista.senha)
            email = ciclista.email

            # Validação dos dados
            if not self.validar_dados_ciclista(ciclista):
                return {"error": "Dados inválidos"}, 422
            
            self.enviar_email(email,"Cadastro alterado com sucesso")
            return ciclista.to_dict()


    def validar_dados_ciclista(self, ciclista):
        if ciclista.nacionalidade == "Brasileiro" and not ciclista.cpf:
            return False
        
        return True
    
    
    def obter_ciclista_por_id(self, id_ciclista):
        for Ciclista in self.ciclistas:
            if Ciclista.id_ciclista == id_ciclista:
                return Ciclista
        return None   
    
    
    
    
    
    # PRIMEIRA ENTREGA
    
    def cadastrar_ciclista(self, data):
        response_mock = Mock()
        response_mock.status_code = "Dados cadastrados", 200

        validacao = True
        if not validacao:
            response_mock.status_code = 422
            response_mock.json.return_value = [{
                "codigo": 422,
                "mensagem": "Dados inválidos"
            }]
            return response_mock.json()

        self.validar_cartao()

        response_mock.json.return_value = self.dados_ciclista(data)
        return response_mock.json()

    def dados_ciclista(self, data):
        nome = data.get("ciclista").get("nome")
        nascimento = data.get("ciclista").get("nascimento")
        cpf = data.get("ciclista").get("cpf")
        passaporte_numero = data.get("ciclista").get("passaporte").get("numero")
        passaporte_validade = data.get("ciclista").get("passaporte").get("validade")
        passaporte_pais = data.get("ciclista").get("passaporte").get("pais")
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
    def ativar_ciclista(self, id_ciclista):
        response_mock = Mock()
        response_mock.status_code = 200

        ciclistas = self.listar_ciclistas()
        for ciclista in ciclistas:
            if ciclista['id_ciclista'] == id_ciclista:
                ciclista['status'] = 'ativado'
                return ciclista

        return {'error': 'Ciclista not found'}, 404

    def listar_ciclistas(self):
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

    # Método de enviar email (retornando sempre "sucesso"), mas que não chame o microsserviço Externo.
    # def enviar_email(self):
    #     response_mock = Mock()
    #     response_mock.json.return_value = {"message": "Email enviado com sucesso"}
    #     return response_mock.json()
    
    
    
    # Método de enviar email (retornando sempre "sucesso"), mas que não chame o microsserviço Externo.
    def enviar_email(self, email, mensagem):
        send_to = email;
        body = mensagem;
        return True;

    # Apenas para retornar sem chamar o microsserviço externo
    def validar_cartao(self):
        return True
