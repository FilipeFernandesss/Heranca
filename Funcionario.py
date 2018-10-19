#Classe Funcionario
#IMportando a classe Pessoa

from Pessoa import Pessoa

class Funcionario(Pessoa):
    #Metodo construtor da classe filha
    def __init__(self, nome, cpf, idade, matricula, salario, setor):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.salario = salario
        self.setor = setor

#Sobrescrever metodo str
    def __str__(self):
        return f'{super().__str__()}, Matricula: {self.matricula}, Salário: {self.salario}, Setor: {self.setor}'