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
    

    def gerarDataFrame(self):

        return pd.DataFrame(self.organizarData())

    def save(self):

        self.formatData()

        nomeArquivo = self.dicionario[0]["Turma"] + " " + str(self.data) + ".xlsx"

        self.gerarDataFrame().to_excel(nomeArquivo, index=True)

    def organizarData(self):
        
        keys, values = self.getItemsDict()

        data = {"Nome": keys[1:], "Situação": values[1:], "Turma": values[0], "Data": str(self.data)}

        return data

    def formatData(self):

        data = list(self.data)

        for i in range(len(data)):
            if data[i] == '/':
                data[i] = '-'
        data = ''.join(data)
        self.data = data



