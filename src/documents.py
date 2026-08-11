import requests
from datetime import datetime
session = requests.Session()
def loadDocuments (): 
    today = datetime.now().strftime("%d/%m/%Y")
    url = f"https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosDados"
    params = {
        "d": 1,
        "s": 0,
        "l": 200,
        "o[0][dataEntrega]": "desc",
        "tipoFundo": 1,
        "dataInicial": '15/07/2026',
        "dataFinal": '15/07/2026'
    }
    #https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosDados?d=1&s=0&l=20&dataInicial=17/07/2026&dataFinal=17/07/2026&l=200
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentos",
        "Connection": "keep-alive"
    }
    print(f"Buscando documentos de {today}...")
    response = session.get(url, params=params, headers=headers, timeout=10)
    data = response.json()
    documents = data.get("data")
    for doc in documents:
        print("=== NOVO DOCUMENTO ENCONTRADO ===")
        for chave, valor in doc.items():
            print(f"{chave}: {valor}")
        print("=" * 35)
    
    print('Lenghth: ', len(documents))
        
        
        
        
        
    #print (documents)
    
    
if __name__ == '__main__':
    print('Loading')
    loadDocuments()