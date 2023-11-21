class MeioDePagamento:
    def __init__(self, nome_titular, numero_cartao, validade_cartao, cvv_cartao, ciclista):
        self.nome_titular = nome_titular
        self.numero_cartao = numero_cartao
        self.validade_cartao = validade_cartao
        self.cvv_cartao = cvv_cartao
        self.ciclista = ciclista  

    def to_dict(self):
        return {
            "nome_titular": self.nome_titular,
            "numero_cartao": self.numero_cartao,
            "validade_cartao": self.validade_cartao,
            "cvv_cartao": self.cvv_cartao,
            "ciclista": self.ciclista.to_dict() if self.ciclista else None
        }
