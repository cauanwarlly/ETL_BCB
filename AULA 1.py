class Empresa:
    def __init__(self, nome="Turma 34"):
        self.nome = nome
        self.pilares = []
        self.funcionarios = []

    def cadastrar_pilar(self, nome, descricao):
        self.pilares.append({"nome": nome, "descricao": descricao})

    def consultar_pilares(self):
        print(f"Pilares da empresa {self.nome}:")
        for pilar in self.pilares:
            print(f" - Pilar: {pilar['nome']}, Descrição: {pilar['descricao']}")

    def cadastrar_funcionario(self, nome, salario):
        self.funcionarios.append({"nome": nome, "salario": salario})

    def consultar_funcionarios(self):
        print(f"Funcionários da empresa {self.nome}:")
        for funcionario in self.funcionarios:
            print(f" - Funcionário: {funcionario['nome']}, Salário: R$ {funcionario['salario']:.2f}")


# uso
emp = Empresa()
emp.cadastrar_pilar("Ética", "Agir de forma correta e justa")
emp.cadastrar_funcionario("João", 3500)

emp.consultar_pilares()
emp.consultar_funcionarios()
