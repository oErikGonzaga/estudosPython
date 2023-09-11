def converter_mes_extenso(data):
    mes = '''janeiro fevereiro março
             abril maio junho
             julho agosto setembro
             outubro novembro dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1]
    return f'{d} de {mes_extenso} de {a}'


print(converter_mes_extenso('10/05/2021'))
