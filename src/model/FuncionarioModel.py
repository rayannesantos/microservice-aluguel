class Funcionario:
    def __init__(self, id_funcionario, matricula, senha, email, nome, idade, funcao, cpf, confirmacaoSenha=None):
        self.id_funcionario = id_funcionario
        self.matricula = matricula
        self.senha = senha
        self.confirmacaoSenha = confirmacaoSenha
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
            "confirmacaoSenha": self.confirmacaoSenha,
            "email": self.email,
            "nome": self.nome,
            "idade": self.idade,
            "funcao": self.funcao,
            "cpf": self.cpf
        }
