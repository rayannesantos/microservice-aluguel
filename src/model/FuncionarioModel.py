class Funcionario:
    def __init__(self, id_funcionario, matricula, senha, email, nome, idade, funcao, cpf, confirmacao_senha=None):
        self.id_funcionario = id_funcionario
        self.matricula = matricula
        self.senha = senha
        self.confirmacao_senha = confirmacao_senha
        self.email = email
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.cpf = cpf

    def to_dict(self):
        return {
            "id_funcionario": self.id_funcionario,
            "matricula": self.matricula,
            "senha": self.senha,
            "confirmacaoSenha": self.confirmacao_senha,
            "email": self.email,
            "nome": self.nome,
            "idade": self.idade,
            "funcao": self.funcao,
            "cpf": self.cpf
        }
