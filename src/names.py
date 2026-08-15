import pandas as pd
db_fundos = pd.read_excel("files/FundosNomes.xlsx", header=None, 
    names=['Nome', 'NomePregao', 'ticker'])
names = []
def getNames(ticker): 
    names = []
    ticker_limpo = ticker.removesuffix("11").upper()
    #print(ticker_limpo)
    nome_fundo = db_fundos.loc[db_fundos['ticker'] == ticker_limpo, 'Nome'].item()
    nome_fundo_pregao = db_fundos.loc[db_fundos['ticker'] == ticker_limpo, 'NomePregao'].item()
    names.append(nome_fundo)
    names.append(nome_fundo_pregao)
    return names
    

    
        
if __name__ == '__main__':
    names = getNames('hglg11')
    print(names)
   