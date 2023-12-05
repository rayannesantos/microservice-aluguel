from datetime import datetime, timedelta

class AluguelBicicleta:
    def __init__(self, bicicleta, hora_inicio, tranca_inicio, hora_fim=None, tranca_fim=None, cobranca=0, status="finalizado com cobrança pendente", ciclista=None):
        if isinstance(hora_inicio, str):
            hora_inicio = datetime.strptime(hora_inicio, "%Y-%m-%d %H:%M:%S")

        self.bicicleta = bicicleta
        self.hora_inicio = hora_inicio
        self.tranca_inicio = tranca_inicio
        self.hora_fim = hora_fim
        self.tranca_fim = tranca_fim
        self.cobranca = cobranca
        self.status = status
        self.ciclista = ciclista

    def to_dict(self):
        return {
            "bicicleta": self.bicicleta,
            "horaInicio": self.hora_inicio.isoformat() if isinstance(self.hora_inicio, datetime) else self.hora_inicio,
            "trancaFim": self.tranca_fim,
            "horaFim": self.hora_fim.isoformat() if self.hora_fim and isinstance(self.hora_fim, datetime) else self.hora_fim,
            "cobranca": self.cobranca,
            "trancaInicio": self.tranca_inicio,
            "status": self.status,
            "ciclista": self.ciclista.to_dict() if self.ciclista else None
        }