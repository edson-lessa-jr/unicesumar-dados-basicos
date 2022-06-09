import json

def importar_arquivo():
    with open("DadosCadastrais.json", encoding='utf-8') as dados_json:
        dados_cadastrais = json.load(dados_json)

    print(dados_cadastrais["value"][0]["dataautorizacao"])

importar_arquivo()