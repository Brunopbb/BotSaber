from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import os
import time

import dados_planilha
import login_usuario
import menuAux


class botSaber:

    

    def __init__(self, login, senha):

        

        self.login = login
        self.senha = senha
        self.NumeroDeDisciplinas = 0

        user = getpass.getuser()
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            self.browser = webdriver.Chrome(executable_path='C:\\Users\\'+str(user)+'\\Desktop\\BotSaber\\chromedriver.exe', options=options)
            
        except Exception:
            pass
    

    def loginSistema(self):

        try:
            driver = self.browser

            driver.get("http://saber.pb.gov.br/users/sign_in")
            campo_usuario = driver.find_element_by_xpath("//*[@id='user_email']")
            campo_usuario.send_keys(self.login)
            time.sleep(1)
            campo_senha = driver.find_element_by_xpath("//*[@id='user_password']")
            campo_senha.click()
            campo_senha.send_keys(self.senha)
            campo_senha.send_keys(Keys.ENTER)
        except Exception:
            pass
        

    
    def GetNDisciplinas(self):

        driver = self.browser
        cont = 0
        while True:
            cont+=1
            try:
                driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/table/tbody/tr["+str(cont)+"]/td[3]").text       
            except Exception:
                break
        
        self.NumeroDeDisciplinas = cont
    
    def getNomeAlunos(self, turmaSelecionada, Nmatriculas, driver):

        nomes = []
        
        for i in range(1, int(Nmatriculas[turmaSelecionada-1])+1):
            nomes.append(driver.find_element_by_xpath("/html/body/div[5]/div/form/div[3]/div["+str(i)+"]/div[1]").text)

        return nomes
        
    def registrarFaltas(self, nomes, turmaSelecionada, listaDisciplinas):
        
        os.system("cls||clear")
        FaltasRegistradas = {}

        FaltasRegistradas["Turma"] = listaDisciplinas[turmaSelecionada-1]
 
        for alunos in nomes:
            
            print("----------------------------------------------------------------")
            print(alunos, end=' -----> ')
            entrada = input("Presente(P), Ausente(F), Não Registrado(N): ").upper()
            

            while entrada != 'P' and entrada != 'F' and entrada != 'N':
                print("Entrada invalida!")
                print("----------------------------------------------------------------")
                print(alunos, end=' -----> ')
                entrada = input("Presente(P), Ausente(F), Não Registrado(N): ").upper()
                

            FaltasRegistradas[alunos] = entrada

        
        return FaltasRegistradas

    
    def menu(self, listaDisciplinas):
        os.system("cls||clear")
        print("#### Suas disciplinas ####")
        for i in range(self.NumeroDeDisciplinas-1):
            print(i+1, end=" ---> ")
            print(listaDisciplinas[i])

        turmaSelecionada = int(input("Digite o numero da turma: "))
        return turmaSelecionada

    def getInfoDisciplinas(self):

        driver = self.browser
        listaDisciplinas = []
        cargaHoraria = []
        Nmatriculas = []
        
        num = self.NumeroDeDisciplinas

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
            if(turmaSelecionada > self.NumeroDeDisciplinas or turmaSelecionada < 1):
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

    def gerarPlanilha(self, save):

        planilha = dados_planilha.Planilha(save)
        planilha.getItemsDict()
        planilha.organizarData()
        planilha.gerarDataFrame()
        planilha.save()

    def menuPrincipal(self, menus):

        driver = self.browser
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
                self.gerarPlanilha(save)
            
            
            op = menus.menuMenuPrincipal()

            if(op == 'S'):
                self.returnPaginaInicial(driver)
                flag = True
            else:
                break
        
    
menus = menuAux


login = login_usuario.login_saber
myBot = botSaber(login["usuario"], login["senha"])
myBot.loginSistema()


while True:
 
    os.system('cls||clear')
    menus.menuEntrada()
    opcao = input("REGISTRAR FALTAS DAS TURMAS? SIM(S), NÃO(N): ").upper()

    if(opcao == 'S'):
        myBot.menuPrincipal(menus)
    else:
        break

print("Encerrando...")
time.sleep(2)


