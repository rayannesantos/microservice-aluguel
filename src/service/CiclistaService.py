# UC01–Cadastrar Ciclista
from unittest.mock import Mock
from model.CiclistaModel import Ciclista
from model.MeiodePagamentoModel import MeioDePagamento  # Make sure to adjust the import path

class CiclistaService: 
    def __init__(self):
        # Inicializa com alguns dados fictícios de ciclistas
        self.ciclistas_data = [
            {
                "id_ciclista": 3,
                "nome": "Ciclista 1",
                "nascimento": "nascimento",
                "cpf": "",
                "passaporte": {
                    "numero": "12358",
                    "validade": "02/01/1997",
                    "pais": "MX"
                },
                "nacionalidade": "ESTRANGEIRO",
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
        self.ciclistas = []
        
        for ciclista_data in self.ciclistas_data:
            ciclista = Ciclista(**ciclista_data)

            if not self.ciclistas:  
                meio_de_pagamento_data = {
                    "nome_titular": "Titular",
                    "numero_cartao": "1234567890123456",  
                    "validade_cartao": "2025-12-31",
                    "cvv_cartao": "123",
                    "ciclista": ciclista  
                }
                
                ciclista.meio_de_pagamento = MeioDePagamento(**meio_de_pagamento_data)

            self.ciclistas.append(ciclista)
            
            

    def listar_todos(self):
        ciclistas = [ciclista.to_dict() for ciclista in self.ciclistas]
        return ciclistas        
    
    def listar_meio_de_pagamento_por_id(self, id_ciclista):
        ciclista = self.obter_ciclista_por_id(id_ciclista)

        if ciclista:
            meio_de_pagamento = ciclista.meio_de_pagamento
            if meio_de_pagamento:
                return meio_de_pagamento.to_dict()

        return {"error": "Ciclista or meio de pagamento not found"}, 404
    

    # UC06 – Alterar Dados do Ciclista
    def alterar_ciclista(self, id_ciclista, dados):
        ciclista = self.obter_ciclista_por_id(id_ciclista)
        
        if ciclista:
            # Atualiza os dados do ciclista com os novos dados
            # Verifica se o ciclista é brasileiro e se o CPF está presente
            if ciclista.nacionalidade == "BRASILEIRO" and not dados.get("cpf"):
                return {"error": "CPF é obrigatório para ciclistas brasileiros"}, 422

            ciclista.nome = dados.get("nome", ciclista.nome)
            ciclista.cpf = dados.get("cpf", ciclista.cpf)
            ciclista.passaporte = dados.get("passaporte", ciclista.passaporte)
            ciclista.nacionalidade = dados.get("nacionalidade", ciclista.nacionalidade)
            ciclista.url_foto_documento = dados.get("url_foto_documento", ciclista.url_foto_documento)
            ciclista.senha = dados.get("senha", ciclista.senha)

            # Validação dos dados
            if not self.validar_dados_ciclista(ciclista):
                return {"error": "Dados inválidos"}, 422
            
            self.enviar_email()
            return ciclista.to_dict()
        
        return {"error": "Ciclista não encontrado"}, 404


    def validar_dados_ciclista(self, ciclista):
        if ciclista.nacionalidade == "Brasileiro" and not ciclista.cpf:
            return False
        
        return True
    
    
    def obter_ciclista_por_id(self, id_ciclista):
        for ciclista in self.ciclistas:
            if ciclista.id_ciclista == id_ciclista:
                return ciclista
        return None   
    
    
    
    # UC07 – Alterar Cartão
    def alterar_cartao(self, id_ciclista, dados_cartao):
        ciclista = self.obter_ciclista_por_id(id_ciclista)

        if ciclista:
            if not self.validar_dados_cartao():
                return {"error": "Dados do cartão inválidos"}, 422

            if not self.enviar_para_administradora_cc():
                return {"error": "Cartão recusado pela Administradora CC"}, 422

            ciclista.meio_de_pagamento = MeioDePagamento(
                nome_titular=dados_cartao["nome_titular"],
                numero_cartao=dados_cartao["numero_cartao"],
                validade_cartao=dados_cartao["validade_cartao"],
                cvv_cartao=dados_cartao["cvv_cartao"],
                ciclista=ciclista
        )

            if not self.enviar_email():
                return {"warning": "Cartão atualizado, mas houve um problema ao enviar o e-mail"}

            return {"success": "Cartão atualizado com sucesso"}

        return {"error": "Ciclista não encontrado"}, 404


    def validar_dados_cartao(self):
        # externo
        return True

    def enviar_para_administradora_cc(self):
        # Simulação do envio para a Administradora CC
        return True


    # PRIMEIRA ENTREGA
    def cadastrar_ciclista(self, data):
        response_mock = Mock()
        response_mock.status_code = 200  # Assume success by default
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

       
    # Apenas para retornar sem chamar o microsserviço externo
    def enviar_email(self):
        return True
    
    # Apenas para retornar sem chamar o microsserviço externo
    def validar_cartao(self):
        return True
