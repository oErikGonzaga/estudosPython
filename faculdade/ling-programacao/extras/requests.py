import requests


# Endpoint da API
url = "https://api.exemplo.com/endpoint"

# Parâmetros para a requisição GET (se houver)
params = {
    'parametro1': 'valor1',
    'parametro2': 'valor2'
}

try:
    # Faz a requisição GET
    response = requests.get(url, params=params)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Converte a resposta para JSON (se a resposta for em JSON)
        data = response.json()
        print('Resposta da API:')
        print(data)
    else:
        print('Erro na requisição. Código de status:', response.status_code)

except requests.exceptions.RequestException as e:
    print('Erro ao fazer a requisição:', e)
