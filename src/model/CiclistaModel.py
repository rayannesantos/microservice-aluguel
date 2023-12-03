class Ciclista:
    def __init__(self, id_ciclista, nome, nascimento, cpf, passaporte, nacionalidade, email, url_foto_documento, senha):
        self.id_ciclista = id_ciclista
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.passaporte = passaporte
        self.nacionalidade = nacionalidade
        self.email = email
        self.url_foto_documento = url_foto_documento
        self.senha = senha
        self.status_aluguel = False


    def to_dict(self):
        return {
            "id_ciclista": self.id_ciclista,
            "nome": self.nome,
            "nascimento": self.nascimento,
            "cpf": self.cpf,
            "passaporte": self.passaporte,
            "nacionalidade": self.nacionalidade,
            "email": self.email,
            "url_foto_documento": self.url_foto_documento,
            "senha": self.senha,        
            "status_aluguel": self.status_aluguel

        }

