#Classe Aluno
#Importando a classe Pessoa
from Pessoa import Pessoa

#Criando a classe filha 'Aluno'
class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, curso, turno, ra):
        super().__init__(nome, cpf, idade)
        self.curso = curso
        self.turno = turno
        self.ra = ra

    #Sobrescrevendo o metodo str
    def __str__(self):
        return f'{super().__str__()}, Curso: {self.curso}, Turno: {self.turno}, RA: {self.ra} '