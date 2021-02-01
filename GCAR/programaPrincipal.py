from sistema import *
from acompArquivo import *
from time import sleep

arq = 'concessionariaGCAR.txt'
if not arqExist(arq):
    createArq(arq)

while True:
    answer = menu(['LISTAR VEÍCULOS', 'CADASTRAR VEÍCULOS', 'DAR BAIXA', 'SAIR DO SISTEMA'])
    if answer == 1:
        # Opção de listar o conteúdo da lista
        readArq(arq)
    elif answer == 2:
        # Opção de cadastrar um novo item a lista
        header('NOVO CADASTRO DE VEÍCULO')
        brand = str(input('MARCA: ')).upper()
        model = str(input('MODELO: ')).upper()
        year = int(input('ANO: '))
        color = str(input('COR: ')).upper()
        milage = int(input('Km RODADO: '))
        fuel = str(input('TIPO DE COMBUSTÍVEL: ')).upper()
        price = int(input('VALOR DO VEÍCULO: R$'))
        register(arq, brand, model, year, color, milage, fuel, price)
    elif answer == 3:
        # Exclui determinado item da lista
        readArq(arq)
        header('PARA A BAIXA DIGITE O NÚMERO DO VEÍCULO')
        modelLine = int(input('\033[1;32mDIGITE O NÚMERO PARA BAIXA (Começa no 0): \033[m'))
        readDelArq(arq, modelLine)
        
    elif answer == 4:
        header('SAINDO DO SISTEMA... ATÉ LOGO')
        break
    else:
        print('\033[1;31mERR: DIGITE UMA OPÇÃO VÁLIDA!\033[m')
    sleep(2)
