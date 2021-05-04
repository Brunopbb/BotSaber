import pandas as pd

class Planilha:

    def __init__(self, dicionario, data):
        self.dicionario = dicionario
        self.data = data

    def getItemsDict(self):
    
        keys = []
        values = []
    
        for k, v in self.dicionario[0].items():
            keys.append(k)
            values.append(v)
    
    
        return keys, values
    
    def setDict(self, dicionario):
        self.dicionario = dicionario

    def getDict(self):
        return self.dicionario


    def gerarDataFrame(self):

        return pd.DataFrame(self.organizarData())

    def save(self):

        self.gerarDataFrame().to_excel('saida.xlsx', index = True)

    def organizarData(self):
        
        keys, values = self.getItemsDict()

        data = {"Nome": keys[1:], "Situação": values[1:], "Turma": values[0], "Data": self.data}

        return data


