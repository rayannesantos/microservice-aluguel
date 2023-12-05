class MeioDePagamento:
    def __init__(self, nome_titular, numero, validade, cvv, ciclista):
        self.nome_titular = nome_titular
        self.numero = numero
        self.validade = validade
        self.cvv = cvv
        self.ciclista = ciclista  

    def to_dict(self):
        return {
            "nome_titular": self.nome_titular,
            "numero": self.numero,
            "validade": self.validade,
            "cvv": self.cvv,
            "ciclista": self.ciclista.to_dict() if self.ciclista else None
        }
