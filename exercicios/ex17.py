Lista_nome = []
print("Digite (s) para sair")
while True:
    nome = str(input("Digite um nome: "))
    if nome == "s" or nome == "S":
        break
    Lista_nome.append(nome)
x = 0
while x < len(Lista_nome):
    print(Lista_nome[x])
    x += 1
