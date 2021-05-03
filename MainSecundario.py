print("########## Menu de registro de faltas #########")
root = botSaber() # pq essa linha ta errada? não existe um metodo/funçao "botSaber"


salvaFaltas = {}
#Aqui inicializar o bot
#Fazer o login, entrar nas opções de turma e escolher a turma
root.login_saber 
print("Escolha a turma >")
turma = input()
numero_disciplinas = root.GetNDisciplinas()
menu = root.menu(root.getListaDisciplinas(), turma)
#Aqui encontra os alunos
#Perguntar se é uma ou duas turmas:
print("Registrar uma ou duas faltas? >")
registro = int(input())
if registro == 1:
    for i in range(len(root.getListaDeAlunos())):  #Tentar transformar a lista em atributo pra poder usar get
        # esse menu de escolha pode ser um método
        print("Escolha uma opção >")
        print("(F)alta")
        print("(P)resença")
        print("(N)ão registrado")
        opcao = input()
        #Aqui achar uma forma de deixar salvo no dicionario
    root.umaAula()
elif regitro == 2:
    for i in range(len(root.getListaDeAlunos())):
        # esse menu de escolha pode ser um método
        print("Escolha uma opção >")
        print("(F)alta")
        print("(P)resença")
        print("(N)ão registrado")
        opcao = input()
        #aqui tem  que chamar o método que vc  dá a opção de input
        #Aqui achar uma forma de deixar salvo no dicionario
    root.duasAulas()


#repete em loop e a cada entrada dada, salva a informação no dicionário

while True:
    print("Repetir os dados em uma nova turma? (S)im ou (N)ão>")
    entrada = input().upper()

    if entrada == "N":
        break
    #aqui eu chamaria todos os métodos qe ja existem e fazem o registro, usando o proprio dicionario que criei no main
    #como parametro pra os metodos uma e duas aulas.
