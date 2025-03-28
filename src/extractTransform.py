import requests 
import pandas as pd

#print (req.status_code)

#print(req.json())

def requestApiBCB(data: str )-> pd.DataFrame:
    """
    funçao para estrair os dados do banco central
    
    parametros:
    data - string - AAAAT (Exemplo: 20191)
    
    Saida:
    DataFrame - Estrutura de dados do pandas
    
    teste
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    
    req = requests.get(url)
    print("Status Code:", req.status_code)
    dados = req.json()
    
    df = pd.json_normalize(dados['value'])
    df['datatrimestre'] = pd.to_datetime(df['datatrimestre'])
    return df
dadosBcd = requestApiBCB('20191')
