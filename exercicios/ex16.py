soma = 0
sair = "n"
while True:
    num = int(input("Digite um número para somar: "))
    sair = str(input("Quer sair: (s/n) "))
    soma += num
    if sair == "s":
        break
print(soma)
