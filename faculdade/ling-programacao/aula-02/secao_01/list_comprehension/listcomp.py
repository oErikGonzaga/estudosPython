linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]

# linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
# Essa sintaxe produz o mesmo resultado que a linha 1

print("Antes da listcomp = ", linguagens)

# listcomp pythônica de criar uma lista com base em um objeto iterável
linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)

# Esse tipo de técnica é utilizado quando, dada uma sequência,
# deseja-se criar uma nova sequência,
# porém com as informações originais transformadas ou filtradas por um critério
