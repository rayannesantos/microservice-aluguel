class Ciclista:
    def __init__(self, id_ciclista, status, nome, nascimento, cpf, passaporte, nacionalidade, email, urlFotoDocumento):
        self.id_ciclista = id_ciclista
        self.status = status
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.passaporte = passaporte
        self.nacionalidade = nacionalidade
        self.email = email
        self.urlFotoDocumento = urlFotoDocumento


# Dados fornecidos
dados_ciclista_1 = {
    "id_ciclista": 1,
    "status": "desativado",
    "nome": "Ciclista 1",
    "nascimento": "2023-11-13",
    "cpf": "00964211258",
    "passaporte": {
        "numero": "123456",
        "validade": "2023-11-13",
        "pais": "JF"
    },
    "nacionalidade": "Brasileiro",
    "email": "ciclista1@example.com",
    "urlFotoDocumento": "foto1.jpg"
}

dados_ciclista_2 = {
    "id_ciclista": 2,
    "status": "desativado",
    "nome": "Ciclista 2",
    "nascimento": "2023-11-13",
    "cpf": "00964211258",
    "passaporte": {
        "numero": "654321",
        "validade": "2023-11-13",
        "pais": "JF"
    },
    "nacionalidade": "Brasileiro",
    "email": "ciclista2@example.com",
    "urlFotoDocumento": "foto2.jpg"
}


ciclistas = [Ciclista(**dados_ciclista_1), Ciclista(**dados_ciclista_2)]

primeiro_ciclista = ciclistas[0]
