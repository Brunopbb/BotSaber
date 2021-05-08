import time
import os

def menuEntrada():

    #os.system('cls||clear')
    print("#################################################")
    print("SISTEMA DE CONTROLE DE FALTAS - SABER")
    print("#################################################")
    time.sleep(2)

def menuData():

    os.system("cls||clear")
    print("#################################################")
    print("INFORME A DATA DA AULA (dd/mm/aaaa): ")
    print("#################################################")

def menuLogin():

    os.system('cls||clear')
    print("#################################################")
    print("INSIRA SEUS DADOS PARA FAZER LOGIN NO SISTEMA")
    print("#################################################")
    print("\n")

def menuSave():
    os.system('cls||clear')
    print("#################################################")
    op = input("DESEJA SALVA A PLANILHA COM FALTAS? SIM(S), NÃO(N): ").upper()
    print("#################################################")
    return op

def menuJust():

    os.system('cls||clear')
    print("#################################################")
    print("ADICIONE A JUSTIFICATIVA DA AULA: ")
    print("#################################################")


def menuMenuPrincipal():

    print("##########################################################################")
    op = input("DESEJA USAR OS REGISTROS DE FALTAS EM OUTRA TURMA? SIM(S), NÃO(N): ").upper()
    print("##########################################################################")
    return op







