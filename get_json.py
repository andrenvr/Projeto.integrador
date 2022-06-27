import requests
import json
dado = requests.get('http://18.211.70.249/API_enchentes/V0/dado.php')
dados = requests.get('http://18.211.70.249/API_enchentes/V0/dados.php')
print(dado.status_code)
print(dado.headers['content-type'])
print(dado.encoding)
print(dado.json())
data=json.loads(dado.content)#inicio da quebra do json em lista
#[{"id":65,"Temperatura":11,"Pressao":922,"Umidade":42,"Altura":7,"timestamp":"26-06-2022 15:30:47"}]
print(type(dado.json()))
print(data)
temperatura=data[0]['Temperatura']#pega a temperatura
pressao=data[0]['Pressao']#pega pressão
umidade=data[0]['Umidade']#pega umidade
altura=data[0]['Altura']#pega altura
timestamp=data[0]['timestamp']# pega timestamp
print(temperatura)
print(pressao)
print(umidade)
print(altura)
print(timestamp)

