#Classe Professor
#Import Pessoa
from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, cpf, idade, disciplina, matricula, salario):
        super().__init__(nome, cpf, idade)
        self.disciplina = disciplina
        self.matricula = matricula
        self.salario = salario

    def __str__(self):
        return f'{super().__str__()}, Disciplina: {self.disciplina}, Matricula: {self.matricula}, Salario: {self.salario}'
