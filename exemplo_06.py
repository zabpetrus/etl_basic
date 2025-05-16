import requests
from tinydb import TinyDB
from datetime import datetime
import time


def load(dados_tratados):
    try:
        db = TinyDB('db.json')
        db.insert(dados_tratados)
        print("Dados salvos")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


def extrair():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()


def transformar(dados_json):
    valor = dados_json['data']['amount']
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": datetime.now().isoformat()
    }

    return dados_tratados


if __name__ == "__main__":
    while True:
        dados_json = extrair()
        dados_tratados = transformar(dados_json)
        load(dados_tratados)
        time.sleep(15)
