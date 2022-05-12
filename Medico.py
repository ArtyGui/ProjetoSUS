from Paciente import *

FAIL = '\033[91m'
RESET = '\033[0m'


def medico():
    print('Você é Dentista, Pediatra ou Cliníco Geral?')
    especialidade = input('').upper()
    if especialidade == 'DENTISTA':
        print('Seus pacientes são: ')
        for paciente in pacienteDentista:
            print(paciente)
        pacienteAtendido = consultar()
        print(pacienteDentista[pacienteAtendido])


    elif especialidade == 'CLINICO GERAL':
        print('Seus pacientes são: ')
        for paciente in pacienteClinicoGeral:
            print(paciente)
        pacienteAtendido = consultar()
        print(pacienteClinicoGeral[pacienteAtendido])

    elif especialidade == 'PEDIATRA':
        print('Seus pacientes são: ')
        for paciente in pacientePediatra:
            print(paciente)
        pacienteAtendido = consultar()
        print(pacientePediatra[pacienteAtendido])

    else:
        print(FAIL+'RESPOSTA INVÁLIDA, TENTE NOVAMENTE'+RESET)
        medico()


def consultar():
    print('Qual paciente você irá consultar')
    nome = input('')
    return nome
