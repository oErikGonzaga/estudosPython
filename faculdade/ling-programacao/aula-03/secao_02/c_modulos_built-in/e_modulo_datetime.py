# O módulo datetime fornece classes para manipular datas e horas.
import datetime as dt

# A sintaxe para acessar os métodos deve ser algo similar a: modulo.classe.metodo()

# Operações com data e hora

hoje = dt.datetime.today()
ontem = hoje - dt.timedelta(days=1)
semana_anterior = hoje - dt.timedelta(weeks=1)

agora = dt.datetime.now()
duas_horas_atras = agora - dt.timedelta(hours=2)

# Formatação

formatar_hoje = dt.datetime.strftime(hoje, "%d-%m-%Y")
formatar_ontem = dt.datetime.strftime(hoje, "%d de %B de %Y")

# Conversão de string para data (o método utilizado aqui é STRPTIME, não confundir com STRFTIME)

data_string = '18/11/2019 15:30'
data_dt = dt.datetime.strptime(data_string, "%d/%m/%Y %H:%M")  # Não há conversão conforme no parâmetro aqui.
data_dt = data_dt.strftime("%d/%m/%Y %H:%M")  # Aqui acontece a formatação (conversão)


print(f'Hoje: {hoje}')
print(f'Ontem: {ontem}')
print(f'Semana anterior: {semana_anterior}')
print(f'Agora: {agora}')
print(f'Duas horas atrás: {duas_horas_atras}')
print(f'Hoje Formatado: {formatar_hoje}')
print(f'Ontem Formatado: {formatar_ontem}')
print(f'String para datetime: {data_dt}')

