deposito_inical = float(input("Digite o depósito inicial da poupança?: "))
taxa_juros = float(input("Digite a taxa de juros da poupança?: "))

taxa_juros = taxa_juros/100

mes = 1
valor_final = deposito_inical
ganhos_juros = 0.00

while mes <= 24:
    ganhos_juros += valor_final*taxa_juros
    valor_final += ganhos_juros
    print(f"No {mes}º sua poupança está em: {valor_final:.2f}")
    print(f"No {mes}º o juros gerou: {valor_final*taxa_juros:.2f}")
    mes += 1
print(f"No total sua poupança em 24 mese acumulou {ganhos_juros:.2f}")
