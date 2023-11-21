 class AluguelService:

    def __init__(self):
  

    def alugar_bicicleta(self, id_ciclista, numero_tranca):
        
        
        
        # ciclista = next((c for c in self.ciclistas if c.id_ciclista == id_ciclista), None)
        # tranca = next((t for t in self.trancas if t.numero_tranca == numero_tranca), None)

        # if ciclista and tranca:
        #     if ciclista.status_aluguel:
        #         # Ciclista já tem um aluguel
        #         return {"error": "Ciclista já tem um aluguel"}

        #     if tranca.status != "ocupada":
        #         # Número da tranca inválido
        #         return {"error": "Número da tranca inválido"}

        #     bicicleta = self.bicicletas[0]  # Assumindo uma única bicicleta para simplificar o exemplo

        #     if bicicleta.status == "em reparo":
        #         return {"error": "A bicicleta não está em condições de uso (status 'em reparo')"}

        #     # Verificar se o pagamento foi autorizado
        #     if self.administradora_cc.processar_pagamento(10.00):
        #         # Atualizar registros
        #         ciclista.status_aluguel = True
        #         bicicleta.status = "em uso"
        #         tranca.status = "livre"

        #         # Registro da retirada da bicicleta
        #         registro_retirada = {
        #             "data_hora_retirada": "timestamp",
        #             "numero_tranca": numero_tranca,
        #             "numero_bicicleta": bicicleta.numero_bicicleta,
        #             "cartao_usado": "1234-5678-9012-3456",
        #             "ciclista": ciclista.nome
        #         }

        #         # Enviar email
        #         self.enviar_email(ciclista, bicicleta, registro_retirada)

        #         return {"success": "Bicicleta alugada com sucesso", "registro_retirada": registro_retirada}

        #     else:
        #         # Erro no pagamento
        #         return {"error": "Erro no pagamento ou pagamento não autorizado"}

        # return {"error": "Ciclista ou tranca não encontrados"}
