import requests as rq
import json

info = rq.get('https://api.github.com/events')

print(info.headers['date'])  # Data de extração
print(info.headers['server'])  # Servidor de origem
print(info.status_code)  # Status HTTP da extração, 200 é ok
print(info.encoding)  # Encoding do texto
print(info.headers['last-modified'])  # Data da última modificação da informação

texto_str = info.text
print(type(texto_str))
print(texto_str[:100])  # exibe somente os 100 primeiros caracteres

texto_json = info.json()
print(type(texto_json))
print(texto_json)
