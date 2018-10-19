#Arquivo princial
from Pessoa import Pessoa
from Funcionario import Funcionario
from Aluno import Aluno
from Professor import Professor

#Objeto da calsse Pessoa
p1 = Pessoa('João', '123', 20)

#Imprimir dados
print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())

#objeto em versao texto
print(p1)

#Objeto funcionario
f1 = Funcionario('José', '456', 40, '0099', 2526.45, 'Biblioteca')

print(f1.get_nome())
print(f1)

#Objeto Aluno

a1 = Aluno('Maria', '789', 19, 'Enfermagem', 'Noturno', '4512345')

print(a1.get_nome())
print(a1)

#Objeto Professor

p1 = Professor('Mario', '159', 56, 'LTPI', '35789', 4054.59)

print(p1.get_nome())
print(p1)