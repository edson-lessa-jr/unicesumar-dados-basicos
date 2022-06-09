import json

with open("data.json", encoding='utf-8') as pessoas_json:
    dados_pessoas = json.load(pessoas_json)

vetor_altura = []
for dados in dados_pessoas:
    string_altura=dados["altura"]
    vetor_altura.append(float(string_altura.replace("," , ".")))

soma=0.0
for i in range(0, len(vetor_altura)):
    soma += vetor_altura[i]

print("A média é: %.2f" % (soma/len(vetor_altura)))