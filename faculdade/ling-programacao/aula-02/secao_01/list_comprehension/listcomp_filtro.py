# Lista que contém somente as linguagens que possuem "Java" no texto
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

linguagens_java = [item for item in linguagens if "Java" in item]


# linguagens_java = [item for item in linguagens if "Java" in item]
# O código acima traria Javascript tambem no resultado.


print(linguagens_java)
