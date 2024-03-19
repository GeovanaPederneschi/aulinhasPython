velocidade = int(input("Digite a velocidade do carro em km/h: "))
if velocidade > 80:
    valor = (velocidade - 80)*5.00
    print("Usúario mutado em R$", valor)
    print(f"Usuário mutado em: R$ {valor:.2f}")
