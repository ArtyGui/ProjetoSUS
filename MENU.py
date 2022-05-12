from Paciente import *
from Medico import *


def menu():
    perg = input('Você é paciente? S/N ').upper()
    if perg == 'S':
        paciente()
    elif perg == 'N':
        medico()
    else:
        print('RESPOSTA INVÁLIDA')
        menu()
