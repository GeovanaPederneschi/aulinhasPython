lista_nome = []
print("Digite (s) para sair")
while True:
    nome = str(input("Digite um nome: "))
    if nome == "s" or nome == "S":
        break
    lista_nome.append(nome)

print(lista_nome)
lista_nome.sort()

x = 0
while x < len(lista_nome):
    print(lista_nome[x])
    x += 1
