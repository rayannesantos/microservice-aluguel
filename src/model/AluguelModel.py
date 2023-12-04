class AluguelBicicleta:
    def __init__(self, bicicleta, hora_inicio, tranca_inicio, hora_fim=None, tranca_fim=None, cobranca=0, ciclista=None):
        self.bicicleta = bicicleta
        self.hora_inicio = hora_inicio
        self.tranca_inicio = tranca_inicio
        self.hora_fim = hora_fim
        self.tranca_fim = tranca_fim
        self.cobranca = cobranca
        self.ciclista = ciclista

    def to_dict(self):
        return {
            "bicicleta": self.bicicleta,
            "horaInicio": self.hora_inicio.isoformat(),
            "trancaFim": self.tranca_fim,
            "horaFim": self.hora_fim.isoformat() if self.hora_fim else None,
            "cobranca": self.cobranca,
            "trancaInicio": self.tranca_inicio,
            "ciclista": self.ciclista.to_dict() if self.ciclista else None  # Assuming Ciclista has a to_dict method
        }
