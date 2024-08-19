import requests
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging
import schedule 
import time
import warnings

#Ignorar a chamada das bibliotecas
warnings.filterwarnings('ignore')
#Configuração básica de loggings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Headers da API
headers = {"chave-api-dados":"a66539aeba5579393d90a5fa6763a215"}

#Função para aplicar a requisão em cada url - lista auxiliar
def request(url):
    response = requests.get(url, headers=headers)
    return response.json()

def coleta(url):
    logging.info('Pegar URL para criação de todas as páginas')
    lista_urls = []
    for i in range(1, 409): 
        lista_urls.append(url + str(i)) 
    array_urls = np.asarray(lista_urls)
    vet_req = np.vectorize(request)
    array_requests = vet_req(array_urls)
    df = np.concatenate(array_requests).tolist()
    return df

def transformar_dados(dado):
    logging.info('Transformando dados e criando dataframe')
    df = pd.DataFrame(df)

    logging.info('Troca de tipo de de colunas')
    coluna_valores = ['valorEmpenhado','valorLiquidado','valorPago','valorRestoInscrito',
        'valorRestoCancelado', 'valorRestoPago']
    for coluna in coluna_valores:
        df[coluna] = df[coluna].str.replace('.','')
        df[coluna] = df[coluna].str.replace(',','.')
        df[coluna] = df[coluna].astype(np.float32)
    
    logging.info('Calculando porcentagem')
    df_area = df[['funcao','valorEmpenhado']]
    area_empenhado = df_area.groupby('funcao').sum('valorEmpenhado')
    porcentagem = (area_empenhado/df_area['valorEmpenhado'].sum())
    
    logging.info('Transformar num data frame') 
    porcentagem = porcentagem.reset_index()
    
def carga(dado):
    dado.to_csv('gov-area-vlrempenhado-2022')

def etl():
  url = 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2022&pagina='
  dado = coleta(url)
  dado = transformar_dados(dado)
  carga(dado)

etl()