from ConcessionariaGCAR.GCAR.sistema import *


def arqExist(name):
    try:
        # r - read; t - text
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createArq(name):
    try:
        # w = write; t = text; + = criar
        a = open(name, 'wt+')
    except:
        print('\033[1;31mERR: HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO\033[m')
    else:
        print(f'ARQUIVO {name} CRIADO COM SUCESSO')


def readArq(name):
    try:
        a = open(name, 'rt')
    except:
        print('\033[1;31mERR: ERRO AO LER O ARQUIVO!\033[m')
    else:
        header('VEÍCULOS CADASTRADOS')
        for lines in a:
            dice = lines.split(',')
            dice[6] = dice[6].replace('\n', '')
            print(f'{dice[0]:.<25}'
                  f'{dice[1]:.<27}'
                  f'{dice[2]:.<10}'
                  f'{dice[3]:.<15}'
                  f'Km {dice[4]:.<13}'
                  f'{dice[5]:.<15}'
                  f'R$ {dice[6]:<10}')
    finally:
        a.close()


def register(arq, brand, model, year, color, milage, fuel, price):
    if milage == 0:
        milage = 'Zero Km'.upper()
    if price == 0:
        price = 'Sob Consulta'.upper()

    try:
        a = open(arq, 'at')
    except:
        print('\033[1;31mERR: HOUVE UM ERRO NA ABERTURA DO ARQUIVO!\033[m')
    else:
        try:
            a.write(f'{brand},{model},{year},{color},{milage},{fuel},{price}\n')
        except:
            print('\033[1;31mERR: HOUVE UM ERRO NO MOMENTO DE ESCREVER OS DADOS\033[m')
        else:
            print(f'\033[1;32mNOVO REGISTRO DE {brand} {model} ADICIONADO\033[m')
            a.close()

def readDelArq(arq, modelLine):
    try:
        a = open(arq, 'rt')
        lines = a.readlines()
    except:
        print('\033[1;31mERR: HOUVE UM ERRO NA ABERTURA DO ARQUIVO\033[m')
    else:
        try:
            del lines[modelLine]
        except:
            print('\033[1;31mERR: HOUVE UM ERRO NA EXCLUSÃO DO ITEM\033[m')
        else:
            new_a = open(arq, "w+")
            for lineList in lines:
                new_a.write(lineList)
                print('\033[1;32mBAIXA REALIZADA COM SUCESSO\033[m')
    finally:
        new_a.close()
