from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import exit
import getpass
import os
import time

import dados_planilha
import login_usuario
import menuAux


class botSaber:


    def __init__(self, login, senha):

        self.__login = login
        self.__senha = senha
        self.__NumeroDeDisciplinas = 0
        self.__browser = None
        

    def setBrowser(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        
        self.__browser = browser


    def loginSistema(self):

        #!Verificar o bloco Try

        try:
            driver = self.__browser

            driver.get("http://saber.pb.gov.br/users/sign_in")
            campo_usuario = driver.find_element_by_xpath("//*[@id='user_email']")
            campo_usuario.send_keys(self.__login)
            time.sleep(1)
            campo_senha = driver.find_element_by_xpath("//*[@id='user_password']")
            campo_senha.click()
            campo_senha.send_keys(self.__senha)
            campo_senha.send_keys(Keys.ENTER)

        except Exception:
            pass
        
    
    def GetNDisciplinas(self):

        driver = self.__browser
        cont = 0
        while True:
            cont+=1
            try:
                driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/table/tbody/tr["+str(cont)+"]/td[3]").text       
            except Exception:
                break
        
        self.__NumeroDeDisciplinas = cont
    
    def getNomeAlunos(self, turmaSelecionada, Nmatriculas, driver):

        nomes = [(driver.find_element_by_xpath("/html/body/div[5]/div/form/div[3]/div["+str(i)+"]/div[1]").text) 
                              for i in range(1, int(Nmatriculas[turmaSelecionada-1])+1)]

        return nomes


    def sair(self):
        #*Encerrar programa
        self.__browser.quit()

    def salvarFaltasSistema(self, driver):
        driver.find_element_by_xpath("/html/body/div[5]/div/form/div[4]/div/button").click()
        
    def registrarFaltas(self, nomes, turmaSelecionada, listaDisciplinas):
        
        os.system("cls||clear")
        FaltasRegistradas = {}

        FaltasRegistradas["Turma"] = listaDisciplinas[turmaSelecionada-1]

        for alunos in nomes:
            while True:
                try:
                    print("---------------------------------------------------------------------------------------")
                    print(alunos, end=' -----> ')
                    entrada = input("Presente(P), Ausente(F), Não Registrado(N): ").upper()
                    if(entrada != 'P' and entrada != 'F' and entrada != 'N'):
                        raise ValueError
                    else:
                        FaltasRegistradas[alunos] = entrada
                        break
                except:
                    print("Entrada invalida!")
        
        return FaltasRegistradas

    
    def menu(self, listaDisciplinas):
        #!Adicionar testes 
        os.system("cls||clear")
        print("#### Suas disciplinas ####")
        for i in range(self.__NumeroDeDisciplinas-1):
            print(i+1, end=" ---> ")
            print(listaDisciplinas[i])

        turmaSelecionada = int(input("Digite o numero da turma: "))
        return turmaSelecionada

    def getInfoDisciplinas(self):

        driver = self.__browser
        listaDisciplinas = []
        cargaHoraria = []
        Nmatriculas = []
        
        num = self.__NumeroDeDisciplinas

        for NumTexto in range(1, num):
            
            listaDisciplinas.append(driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/table/tbody/tr["+str(NumTexto)+"]/td[3]").text+" "+
                                    driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/table/tbody/tr["+str(NumTexto)+"]/td[4]").text)

            cargaHoraria.append(driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/table/tbody/tr["+str(NumTexto)+"]/td[7]").text)
            Nmatriculas.append(driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/table/tbody/tr["+str(NumTexto)+"]/td[9]").text)
            

        return listaDisciplinas, cargaHoraria, Nmatriculas


    def selecionarBotao(self, driver, Nbotao):

        try:

            driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/table/tbody/tr["+str(Nbotao)+"]/td[10]/a").click()
        
        except Exception:
            print("Error!")
        

    def DefNfaltas(self, cargaHoraria, turmaSelecionada):

        #1 --> 1 falta
        #4 --> 2 Falta
        
        if(cargaHoraria[turmaSelecionada-1] == '1'):
            return 1
        elif(cargaHoraria[turmaSelecionada-1] == '4'):
            return 2

    def umaAula(self, nomes, driver):

        count = 0

        
        for aluno in nomes:


            if(nomes[aluno] == 'P'):
    
                driver.find_element_by_xpath("/html/body/div[5]/div/form/div[3]/div["+str(count)+"]/div[2]/div/div/label[1]/input").click()

            elif(nomes[aluno] == 'F'):
                driver.find_element_by_xpath("/html/body/div[5]/div/form/div[3]/div["+str(count)+"]/div[2]/div/div/label[2]/input").click()
            
            elif(nomes[aluno] == 'N'):
                driver.find_element_by_xpath("/html/body/div[5]/div/form/div[3]/div["+str(count)+"]/div[2]/div/div/label[3]/input").click()

            count+=1

        

    def duasAulas(self, nomes, driver):
        

        count = 0

        for aluno in nomes:

            for i in range(1, 3):

                if(nomes[aluno] == 'P'):
        
                    driver.find_element_by_xpath("/html/body/div[5]/div/form/div[3]/div["+str(count)+"]/div[2]/div["+str(i)+"]/div/label[1]/input").click()
                                                
                elif(nomes[aluno] == 'F'):
                    driver.find_element_by_xpath("/html/body/div[5]/div/form/div[3]/div["+str(count)+"]/div[2]/div["+str(i)+"]/div/label[2]/input").click()
            
                elif(nomes[aluno] == 'N'):
                    driver.find_element_by_xpath("/html/body/div[5]/div/form/div[3]/div["+str(count)+"]/div[2]/div["+str(i)+"]/div/label[3]/input").click()

            count+=1

            
    def controleDeFaltas(self, nomes, driver, cargaHoraria):

        if(cargaHoraria == '4'):
            self.duasAulas(nomes, driver)
        elif(cargaHoraria == '1'):
            self.umaAula(nomes, driver)
    
        
    def setFaltas(self, driver, cargaHoraria, turmaSelecionada):

        faltas = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div[2]/form/input[2]")
        faltas.click()
        faltas.send_keys(Keys.CONTROL + "a")
        faltas.send_keys(Keys.DELETE)
        time.sleep(2)
        faltas.send_keys(self.DefNfaltas(cargaHoraria, turmaSelecionada))
        driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[1]/div[2]/form/button").click()
        time.sleep(2) 

    def selecaoDeturma(self, listaDisciplinas):
        while True:
            turmaSelecionada = self.menu(listaDisciplinas)
            if(turmaSelecionada > self.__NumeroDeDisciplinas or turmaSelecionada < 1):
                print("Turma Invalida")
                time.sleep(1)
            else:
                return turmaSelecionada
    
    def returnPaginaInicial(self, driver):

        driver.get("http://saber.pb.gov.br/platform/stats/class_diaries")
        time.sleep(1)

    
    def registrosSalvos(self, FaltasRegistradas):

        turmasRegistradasSaber = []

        turmasRegistradasSaber.append(FaltasRegistradas)

        return turmasRegistradasSaber

    def gerarPlanilha(self, save, data):

        planilha = dados_planilha.Planilha(save, data)
        planilha.getItemsDict()
        planilha.organizarData()
        planilha.gerarDataFrame()
        planilha.save()

    def dataAula(self, driver):

        data = input("-> ")
        time.sleep(2)
        campoData = driver.find_element_by_xpath("/html/body/div[5]/div/form/div[1]/div[1]/div[1]/input")
        campoData.click()
        campoData.send_keys(Keys.CONTROL + "a")
        campoData.send_keys(Keys.DELETE)
        campoData.send_keys(data)

        return data
    
    def justificafivaAula(self, driver):
        just = input("-> ")

        campoJust = driver.find_element_by_xpath("/html/body/div[5]/div/form/div[2]/div/textarea")
        campoJust.click()
        campoJust.send_keys(just)

    def menuPrincipal(self, menus):

        driver = self.__browser
        save = []
        flag = False
        os.system('cls||clear')
        print("Aguarde...")

        while True:
            
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/ul/li[2]/a").click()

            self.GetNDisciplinas()

            listaDisciplinas, cargaHoraria, Nmatriculas = self.getInfoDisciplinas()

            time.sleep(2)

            turmaSelecionada = self.selecaoDeturma(listaDisciplinas)
           

            self.selecionarBotao(driver, turmaSelecionada)

            driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/ul/li[2]/a").click()
            time.sleep(1)

            

            os.system('cls||clear')

            print("Aguarde...")

            self.setFaltas(driver, cargaHoraria, turmaSelecionada)

            menus.menuData()
            data = self.dataAula(driver)
            menus.menuJust()
            self.justificafivaAula(driver)

            nomeAlunos = self.getNomeAlunos(turmaSelecionada, Nmatriculas, driver)
            time.sleep(1)

            if(flag):   
                
                save[0]['Turma'] = listaDisciplinas[turmaSelecionada-1]
                self.controleDeFaltas(save[0], driver, cargaHoraria[turmaSelecionada-1])
                save = []
                
            else:

                
                FaltasRegistradas = self.registrarFaltas(nomeAlunos, turmaSelecionada, listaDisciplinas)
                self.controleDeFaltas(FaltasRegistradas, driver, cargaHoraria[turmaSelecionada-1])

            save = self.registrosSalvos(FaltasRegistradas)

            if(menus.menuSave() == 'S'):
                self.gerarPlanilha(save, data)
                #self.salvarFaltasSistema(driver)
            
            
            op = menus.menuMenuPrincipal()

            if(op == 'S'):
                self.returnPaginaInicial(driver)
                flag = True
            else:
                break
        
    
menus = menuAux

login = login_usuario.login_saber
myBot = botSaber(login["usuario"], login["senha"])
myBot.setBrowser()
myBot.loginSistema()

        
while True:
 
    os.system('cls||clear')
    menus.menuEntrada()
    opcao = input("REGISTRAR FALTAS DAS TURMAS? SIM(S), NÃO(N): ").upper()

    if(opcao == 'S'):
        myBot.menuPrincipal(menus)
    else:
        print("Encerrando...")
        time.sleep(2)
        myBot.sair()
        exit()
        break




