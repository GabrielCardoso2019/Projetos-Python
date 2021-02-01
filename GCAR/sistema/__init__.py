def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERR: POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mINSERÇÃO DE DADOS INTERROMPIDA PELO USUÁRIO.\033[m')
            return 0
        else:
            return n

def line(tam=42):
    return '-' * tam

def header(txt):
    print(line())
    print(txt.center(42))
    print(line())

def menu(list):
    header('MENU PRINCIPAL GCAR')
    cont = 1
    for item in list:
        print(f'\033[1;33m{cont}\033[m -\033[1;34m {item}\033[m')
        cont += 1
    print(line())
    opc = readInt('\033[1;32mSUA OPÇÃO: \033[m')
    return opc
