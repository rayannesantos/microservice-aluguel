# microservice-aluguel


Endpoints:

POST /ciclista Cadastrar um ciclista 


GET /ciclista/{idCiclista} Recupera dados de um ciclista
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/3
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/4


PUT /ciclista/{idCiclista}Alterar dados de um ciclista
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/4
JSON:
{
  "nome": "string",
  "nascimento": "2023-11-19",
  "cpf": "82208467897",
  "passaporte": {
    "numero": "string",
    "validade": "2023-11-19",
    "pais": "MX"
  },
  "nacionalidade": "string",
  "email": "user@example.com",
  "urlFotoDocumento": "string"
}

POST /ciclista/{idCiclista}/ativar Ativar cadastro do ciclista
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/3/ativar

GET /ciclista/{idCiclista}/permiteAluguel Verifica se o ciclista pode alugar uma bicicleta, já que só pode alugar uma por vez.
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/3/permiteAluguel
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/4/permiteAluguel


GET /ciclista/{idCiclista}/bicicletaAlugada  
Retorna bicicleta caso o ciclista tenha alugado ou vazio caso contrário.
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/3/bicicletaAlugada


GET /ciclista/existeEmail/{email} Verifica se o e-mail já foi utilizado por algum ciclista.
true:https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/existeEmail/email@email.com.br
false:https://microservice-aluguel-hm535ksnoq-uc.a.run.app/ciclista/existeEmail/email2@email.com.br

GET /funcionario recupera funcionários cadastrados
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/funcionario

POST /funcionarioCadastrar funcionário

GET /funcionario/{idFuncionario} Recupera funcionário
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/funcionario/1

PUT /funcionario/{idFuncionario} Editar funcionário

DELETE /funcionario/{idFuncionario}Remover funcionário
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/funcionario/2


GET /cartaoDeCredito/{idCiclista} Recupera dados de cartão de crédito de um ciclista
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/cartaoDeCredito/4/

PUT /cartaoDeCredito/{idCiclista}
Alterar dados de cartão de crédito de um ciclista

POST /aluguel Realizar aluguel
https://microservice-aluguel-hm535ksnoq-uc.a.run.app/aluguel
JSON:{
  "id_ciclista": 4,
  "trancaInicio": 100
}

POST 
https://microservice-aluguel-hm535ksnoq-uc.a.run.app//devolucao
Realizar devolução, sendo invocado de maneira automática pelo hardware do totem ao encostar a bicicleta na tranca.

{
	"id_bicicleta": 0,
  "id_tranca": 3
}


