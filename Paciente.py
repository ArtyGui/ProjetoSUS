def paciente():
    global nomePaciente
    nomePaciente = input('Digite seu primeiro nome: ').title()
    print('Agendar uma consulta: Selecione 1 ; Verificar consultas já agendadas: Selecione 2 ')
    pergunta = input('')
    if pergunta == '1':
        agendamento()
    elif pergunta == '2':
        print('Voce tem uma consulta com dentista')
    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
        paciente()


def agendamento():
    print('Agendamento: DENTISTA: Selecione 1, PEDIATRA: Selecione 2, CLINICO GERAL: Selecione 3.')
    pergunta1 = input('')
    if pergunta1 == '1':
        pacienteDentista[nomePaciente] = sintomas()

    elif pergunta1 == '2':
        pacientePediatra[nomePaciente] = sintomas()

    elif pergunta1 == '3':
        pacienteClinicoGeral[nomePaciente] = sintomas()

    else:
        agendamento()


def sintomas():
    sist = []
    febre = input('Você está com Febre? S/N').upper()
    tosse = input('Você está com Tosse? S/N').upper()
    dor_cabeca = input('Você está com Dor de cabeça? S/N').upper()
    moleza = input('Você está com Moleza no corpo? S/N').upper()
    enjoo = input('Você está com Enjoo? S/N').upper()
    if febre == 'S':
        sist.append('febre')

    if tosse == 'S':
        sist.append('Tosse')

    if dor_cabeca == 'S':
        sist.append('Dor de cabeça')

    if moleza == 'S':
        sist.append('Moleza')

    if enjoo == 'S':
        sist.append('Enjoo')
    print('Agendamento completo.')

    return sist


pacienteDentista = {}
pacientePediatra = {}
pacienteClinicoGeral = {}
