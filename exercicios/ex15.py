deposito_inical = float(input("Digite o depósito inicial da poupança?: "))
taxa_juros = float(input("Digite a taxa de juros da poupança?: "))

taxa_juros = taxa_juros/100

mes = 1
valor_final = deposito_inical
ganhos_juros = 0.00
valor_depositado = 0.00

while mes <= 24:
    if mes != 1:
        valor_depositado = float(input(f"Digite o valor depositado no mes {mes}º: "))
    ganhos_juros += (valor_final+valor_depositado)*taxa_juros
    print(f"No {mes}º o juros gerou: {(valor_final+valor_depositado)*taxa_juros:.2f}")
    valor_final += ganhos_juros + valor_depositado
    print(f"No {mes}º sua poupança está em: {valor_final:.2f}")
    mes += 1
print(f"No total sua poupança em 24 mese acumulou {ganhos_juros:.2f}")
