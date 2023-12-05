class Ciclista:
    def __init__(self, id_ciclista, nome, nascimento, cpf, nacionalidade, email, senha, status='aguardando_confirmacao', url_foto_documento=None,passaporte=None):
        self.id_ciclista = id_ciclista
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.passaporte = passaporte
        self.nacionalidade = nacionalidade
        self.email = email
        self.url_foto_documento = url_foto_documento
        self.senha = senha
        self.status = status  
        self.status_aluguel = False
        self.meio_de_pagamento = None

    def to_dict(self, include_status=False):
        ciclista_dict = {
            "id_ciclista": self.id_ciclista,
            "nome": self.nome,
            "nascimento": self.nascimento,
            "cpf": self.cpf,
            "passaporte": self.passaporte,
            "nacionalidade": self.nacionalidade,
            "email": self.email,
            "url_foto_documento": self.url_foto_documento,
            "senha": self.senha,
            "status_aluguel": self.status_aluguel,
            "status": self.status

        }

        if self.meio_de_pagamento:
            ciclista_dict["meio_de_pagamento"] = self.meio_de_pagamento.to_dict()

        if include_status:
            ciclista_dict["status_aluguel"] = self.status_aluguel
            ciclista_dict["status"] = self.status
            
        return ciclista_dict
