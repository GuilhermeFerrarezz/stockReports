import requests
import time
import json
from datetime import datetime
session = requests.Session()

PALAVRAS_CHAVE_FUNDOS = {
    "ZAGROS": "GGRC11",          # Nome atualizado na CVM/B3
    "GUARDIAN": "GARE11",        
    "XP CRÉDITO": "XPCI11",
    "TRX": "TRXF11",
    "RBR PRIVATE": "RBRY11",     # Diferenciação da família RBR
    "RBR MULTI": "RBRX11",       # Diferenciação da família RBR
    "RIZA": "RZTR11",
    "REC RECEBÍVEIS": "RECR11",
    "MÉRITO": "MFII11",
    "TG ATIVO": "TGAR11",
    "RBR RENDIMENTO": "RBRR11"   # Diferenciação da família RBR
}





def loadDocuments (): 
    max_value = 2000
    offset = 0
    today = datetime.now().strftime("%d/%m/%Y")
    data_inicio = '14/07/2026'
    data_final = '19/07/2026'
    url = f"https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosDados"
   
    #https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosDados?d=1&s=0&l=20&dataInicial=17/07/2026&dataFinal=17/07/2026&l=200
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentos",
        "Connection": "keep-alive"
    }
    print(f"Buscando documentos de {today}...")
    all_documents = []
    while offset <= max_value:
        params = {
                "d": 1,
                "s": str(offset),
                "l": 100,
                "o[0][dataEntrega]": "desc",
                "tipoFundo": 1,
                "dataInicial": data_inicio,
                "dataFinal": data_final
            }
        
        try: 
            response = session.get(url, params=params, headers=headers, timeout=10)
            offset += 100
            data = response.json()
            documents = data.get("data", [])
            if not documents:
                print('Não há mais documentos')
                break
            all_documents.extend(documents)
            #print(documents)
            time.sleep(1)
        except Exception as e: 
            print(f'Erro ao buscar página: {e}')
    return all_documents
        
        
        
    
        
        
        
    #print (documents)
    
    
if __name__ == '__main__':
    fundos_wallet = []
    print('Loading')
    all_documents = loadDocuments()
    for doc in all_documents:
                   
                    nome_completo = doc.get("descricaoFundo", "").strip().upper()
                    ticker = None
                    
                    for palavra, sigla in PALAVRAS_CHAVE_FUNDOS.items():
                        if palavra in nome_completo:
                            print("\n=== ALERTA DA SUA CARTEIRA ===")
                            print(f"Fundo Identificado: {sigla}")
                            for chave, valor in doc.items():
                                print(f"{chave}: {valor}")
                            print("=" * 35)
                            
                    
                    
                    
                    
                    
    print('Lenghth: ', len(all_documents))   

    
    with open("resultado_b3.json", "w", encoding="utf-8") as arquivo:
        json.dump(all_documents, arquivo, ensure_ascii=False, indent=4)